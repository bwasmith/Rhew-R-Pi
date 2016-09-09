import Adafruit_DHT

dht_sensor = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, DHT_PIN)

print "Humidity: {:0.1f}%, Temperature: {:0.2f}*C".format(humidity, temperature)
