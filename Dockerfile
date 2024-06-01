FROM python:3.11.9

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]