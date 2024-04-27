FROM python:3.12
LABEL authors="justin"

ADD docker/main.py .

RUN pip install scikit-learn

CMD ['python', './main.py']