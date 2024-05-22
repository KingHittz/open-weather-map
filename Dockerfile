FROM python:latest

RUN apt-get update

RUN apt-get install vim -y

RUN apt-get install nginx -y

WORKDIR /app

COPY  ./requirements.txt /app

RUN pip install -r requirements.txt

COPY ./main.py /app

EXPOSE 8080:80

CMD ["python3", "./main.py"]
