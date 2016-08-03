#!/usr/bin/env python
#Replicate Arduino's AnalogInput tutorial, via Python script and Nanpy library

from time import sleep
from nanpy import ArduinoApi
from nanpy import SerialManager

connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)

sensorPin = 14
ledPin = 13
sensorValue = 0

a.pinMode(ledPin, a.OUTPUT)

print 'Starting Arduino AnalogInput'

while (True):
  #read the value from the sensor:
  sensorValue = a.analogRead(sensorPin)
  #turn the ledPin on
  a.digitalWrite(ledPin, a.HIGH)
  #stop the program for <sensorValue> milliseconds:
  sleep(sensorValue/1000.0)
  # turn the ledPin off:
  a.digitalWrite(ledPin, a.LOW)
  #stop the program for for <sensorValue> milliseconds:
  sleep(sensorValue/1000.0)

  #print out the AnalogRead value at each step:
  #print sensorValue
