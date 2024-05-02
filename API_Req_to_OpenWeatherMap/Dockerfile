FROM python:latest

WORKDIR /app.py

COPY  . /requirements.txt .

RUN pip install -r requirements.txt

COPY . /Req_to_OpenWeatherMap.py /Users/Justin/PycharmProjects/API_Req_to_OpenWeatherMap


CMD ["python3", "./Req_to_OpenWeatherMap.py"]
