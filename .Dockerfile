FROM python:3.9-slim-buster

WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python-dev \
        python-openssl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY main.py .

# Set log level to INFO
ENV LOG_LEVEL=INFO

CMD [ "python", "./main.py" ]
