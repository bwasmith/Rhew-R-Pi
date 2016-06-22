import os, time
import pigpio

pi = pigpio.pi()
import DHT22
s = DHT22.sensor(pi, 4, 17)

s.trigger()
time.sleep(1)
print("Humidity: ", '{:3.2f}'.format(s.humidity() / 1.))
print("Temperature: ", '{:3.2f}'.format(s.temperature() / 1.))

s.cancel()
