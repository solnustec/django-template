import datetime

import pytest
from django.urls import reverse
from django.utils import timezone

from apps.polls.models import Choice, Question


def test_was_published_recently_with_future_question(staff_user):
    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    assert not future_question.was_published_recently()


def test_was_published_recently_with_old_question(staff_user):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    assert not old_question.was_published_recently()


def test_was_published_recently_with_recent_question(staff_user):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)

    assert recent_question.was_published_recently()


@pytest.mark.django_db
def test_was_index_view_no_questions(client):
    response = client.get(reverse("polls:index"))
    assert response.status_code == 200
    assert "No polls are available." in response.content.decode()
    assert list(response.context["latest_question_list"]) == []


@pytest.mark.django_db
def test_was_index_view_past_question(client):
    question = Question.objects.create(
        question_text="Past question.",
        pub_date=timezone.now() - datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:index"))
    assert list(response.context["latest_question_list"]) == [question]


@pytest.mark.django_db
def test_was_index_view_future_question(client):
    Question.objects.create(
        question_text="Future question.",
        pub_date=timezone.now() + datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:index"))
    assert "No polls are available." in response.content.decode()
    assert list(response.context["latest_question_list"]) == []


@pytest.mark.django_db
def test_was_index_view_past_and_future_questions(client):
    past_question = Question.objects.create(
        question_text="Past question.",
        pub_date=timezone.now() - datetime.timedelta(days=30),
    )
    Question.objects.create(
        question_text="Future question.",
        pub_date=timezone.now() + datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:index"))
    assert list(response.context["latest_question_list"]) == [past_question]


@pytest.mark.django_db
def test_was_index_view_two_past_questions(client):
    question1 = Question.objects.create(
        question_text="Past question 1.",
        pub_date=timezone.now() - datetime.timedelta(days=30),
    )
    question2 = Question.objects.create(
        question_text="Past question 2.",
        pub_date=timezone.now() - datetime.timedelta(days=5),
    )
    response = client.get(reverse("polls:index"))
    assert list(response.context["latest_question_list"]) == [question2, question1]


@pytest.mark.django_db
def test_was_detail_view_past_question(client):
    question = Question.objects.create(
        question_text="Past question.",
        pub_date=timezone.now() - datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:detail", args=(question.id,)))
    assert response.status_code == 200
    assert question.question_text in response.content.decode()


@pytest.mark.django_db
def test_was_detail_view_future_question(client):
    question = Question.objects.create(
        question_text="Future question.",
        pub_date=timezone.now() + datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:detail", args=(question.id,)))
    assert response.status_code == 404


@pytest.mark.django_db
def test_was_results_view_past_question(client):
    question = Question.objects.create(
        question_text="Past question.",
        pub_date=timezone.now() - datetime.timedelta(days=30),
    )
    response = client.get(reverse("polls:results", args=(question.id,)))
    assert response.status_code == 200
    assert question.question_text in response.content.decode()


@pytest.mark.django_db
def test_was_vote_view_valid_choice(client):
    question = Question.objects.create(
        question_text="Question.", pub_date=timezone.now() - datetime.timedelta(days=30)
    )
    choice = Choice.objects.create(question=question, choice_text="Choice 1")
    response = client.post(
        reverse("polls:vote", args=(question.id,)), {"choice": choice.id}
    )
    assert response.status_code == 302
    choice.refresh_from_db()
    assert choice.votes == 1
