import time
import Adafruit_DHT
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "<your Azure IoT Hub device connection string>"
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def get_dht_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return {"temperature": temperature, "humidity": humidity}
    else:
        return None

def send_telemetry(device_client, data):
    message = Message(str(data))
    device_client.send_message(message)
    print(f"Sent telemetry: {data}")

def main():
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    while True:
        data = get_dht_data()
        if data:
            send_telemetry(device_client, data)
        time.sleep(5)

if __name__ == '__main__':
    main()
