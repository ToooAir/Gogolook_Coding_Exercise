FROM python:slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD python main.py

EXPOSE 5000