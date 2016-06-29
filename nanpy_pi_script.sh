#!/usr/bin/env python
#LED with 560 Ohm resistor on Pin10 to GND
from nanpy import ArduinoApi
from nanpy import SerialManager
import RPi.GPIO as gpio

connection = SerialManager(device='/dev/ttyACM0')

from time import sleep 

a = ArduinoApi(connection=connection)

LED = 10
a.pinMode(LED, a.OUTPUT)

print "starting"
print "blinking"

for i in range(0, 5):
  a.digitalWrite(LED, a.HIGH)
  sleep(0.5)
  a.digitalWrite(LED, a.LOW)
  sleep(0.5)

print "changing brightness"

bright = 128
a.analogWrite(LED, bright)
sleep(1)
a.digitalWrite(LED, a.HIGH)

for i in range(200):
  bright = bright + 8
  if bright > 200:
    bright = 0
  a.analogWrite(LED, bright)
  sleep(0.05)

a.digitalWrite(LED, a.LOW)
print "Finished"

     
