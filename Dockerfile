FROM python:3.8.5
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED 1
COPY /Travel_agency /code/
COPY requirements.txt /code/Travel_agency/requirements.txt
WORKDIR /code/Travel_agency
RUN pip install -r requirements.txt
EXPOSE 8000