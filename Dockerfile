FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements-dev.txt /code/
RUN pip install -r requirements-dev.txt
COPY . /code/
