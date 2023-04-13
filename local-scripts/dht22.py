import Adafruit_DHT

# Set sensor type and pin number
sensor = Adafruit_DHT.DHT22
pin = 4

# Try to read temperature and humidity from the sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# If reading was successful, print values
if humidity is not None and temperature is not None:
    print('Temperature: {:.1f}°C'.format(temperature))
    print('Humidity: {:.1f}%'.format(humidity))
else:
    print('Failed to get reading. Try again!')
