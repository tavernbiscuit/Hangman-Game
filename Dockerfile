FROM python:3.11.2

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y wget && \
    wget -O gotty.tar.gz https://github.com/yudai/gotty/releases/download/v1.0.1/gotty_linux_amd64.tar.gz && \
    tar -xvf gotty.tar.gz && \
    mv gotty /usr/local/bin/gotty && \
    rm gotty.tar.gz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN chmod +x /usr/local/bin/gotty

EXPOSE 9090

CMD ["gotty", "-w", "-p", "9090", "python", "main.py"]