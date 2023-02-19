import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def settings():
    from django.conf import settings

    return settings


@pytest.fixture()
def staff_user(db):
    """Return a staff member."""
    user = User.objects.create_user(
        username="staff_test",
        email="staff_test@example.com",
        password="password",
        is_staff=True,
        is_active=True,
    )

    return user
