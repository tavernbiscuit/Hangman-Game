FROM python:3.11.2

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 9090

CMD ["python", "app.py"]