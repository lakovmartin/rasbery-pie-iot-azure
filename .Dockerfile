FROM python:3.9-slim-buster

# Set the working directory to /app
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

# Upgrade PIP
RUN pip3 install --upgrade pip setuptools wheel 


# Install Python packages
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy the Python script
COPY main.py .

# Set log level to INFO
ENV LOG_LEVEL=INFO

# Run the Python script.
CMD [ "python3", "-u", "main.py" ]
