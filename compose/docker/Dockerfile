FROM python:3.9

RUN python --version

COPY . /src/
WORKDIR /src

# Install Python dependencies
RUN pip install -U pip
RUN pip install -r requirements-dev.txt

EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
