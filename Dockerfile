FROM python:3.11.2

WORKDIR /app

COPY . /app

CMD ["python", "app.py"]