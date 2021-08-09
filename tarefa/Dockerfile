FROM python:3.8-slim
#FROM centos/python-36-centos7

RUN pip install scikit-learn

RUN pip install pandas

RUN pip install fastapi uvicorn

COPY . /app

WORKDIR /app

ENV FLASH_APP=main.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
