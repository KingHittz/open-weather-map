FROM python:latest

WORKDIR /app

COPY  ./requirements.txt /app

RUN pip install -r requirements.txt

COPY ./main.py /app

CMD ["python3", "./main.py"]
