import time
import os
import json
import Adafruit_DHT
from azure.iot.device import IoTHubDeviceClient, Message
import logging

# Set the logging configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Use the logger to output logs
logging.info('This is an info log')
logging.warning('This is a warning log')
logging.error('This is an error log')

# DHT22 sensor pin
DHT_SENSOR_PIN = 21

# Azure IoT Hub device connection string
connection_string = os.getenv("DEVICE_CONNECTION_STRING")

def send_to_azure_iot_hub(temp, humidity):
    try:
        # create device client
        client = IoTHubDeviceClient.create_from_connection_string(DEVICE_CONNECTION_STRING)

        # create message
        message = Message(json.dumps({"temperature": temp, "humidity": humidity}))

        # send message
        print("Sending message to Azure IoT Hub...")
        client.send_message(message)
        print("Message sent successfully.")
    except Exception as e:
        print("Error sending message: ", e)

while True:
    try:
        # read temperature and humidity data from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT_SENSOR_PIN)

        # send data to Azure IoT Hub
        send_to_azure_iot_hub(temperature, humidity)

        # wait for 10 seconds before sending next data
        time.sleep(10)

    except Exception as e:
        print("Error reading data from sensor: ", e)
