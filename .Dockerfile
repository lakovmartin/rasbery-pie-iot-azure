FROM balenalib/raspberry-pi-python

WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python-dev \
        python-openssl \
    && rm -rf /var/lib/apt/lists/*

# Install required packages for GPIO access
RUN apt-get update && \
    apt-get install -y python-rpi.gpio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Install Adafruit DHT module
RUN pip3 install Adafruit_DHT

COPY main.py .

# Set log level to INFO
ENV LOG_LEVEL=INFO

CMD [ "python3", "./main.py" ]
