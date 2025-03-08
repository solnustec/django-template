FROM python:3.10-alpine

RUN python --version

# Install make
RUN apk add --no-cache make bash

COPY . /src/
WORKDIR /src

# Install Python dependencies
RUN pip install -U pip
RUN pip install -r requirements-dev.txt

EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
