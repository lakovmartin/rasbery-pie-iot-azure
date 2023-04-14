import os
import sys
import time
from azure.iot.device import IoTHubDeviceClient, Message
import Adafruit_DHT

# Read the IoT Hub device connection string from an environment variable.
CONNECTION_STRING = os.environ["IOTHUB_DEVICE_CONNECTION_STRING"]

# Set the DHT22 sensor pin number.
SENSOR_PIN = 4

# Set the time interval in seconds for sending data to Azure IoT Hub.
SEND_INTERVAL = 30

# Set the message format for sending data to Azure IoT Hub.
MESSAGE_FORMAT = '{{"temperature":{0:0.1f},"humidity":{1:0.1f}}}'

def read_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, SENSOR_PIN)
    return temperature, humidity

def send_data_to_iothub(device_client, message):
    try:
        device_client.send_message(message)
        print("Message sent to Azure IoT Hub: {}".format(message))
    except Exception as e:
        print("Error sending message to Azure IoT Hub: {}".format(e))

if __name__ == "__main__":
    try:
        # Initialize the Azure IoT Hub device client.
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

        while True:
            temperature, humidity = read_sensor_data()
            message = MESSAGE_FORMAT.format(temperature, humidity)
            send_data_to_iothub(client, message)
            time.sleep(SEND_INTERVAL)
    except KeyboardInterrupt:
        print("Stopped by the user")
    except Exception as e:
        print("Error: {}".format(str(e)))
