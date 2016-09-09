import Adafruit_DHT
from time import sleep

DELAY_INTERVAL = 5
dht_sensor = Adafruit_DHT.DHT22
DHT_PIN = 4


while True:
  humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, DHT_PIN)

  print "Humidity: {:0.1f}%, Temperature: {:0.2f}*C".format(humidity, temperature)

  sleep(DELAY_INTERVAL)
