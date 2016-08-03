#!/usr/bin/env python 
#simple analog read of pin A0 to light an LED

from nanpy import ArduinoApi
from nanpy import SerialManager

connection = SerialManager(device='/dev/ttyACM0')

a = ArduinoApi(connection=connection)

from time import sleep
analog = 14
LED = 10

a.pinMode(LED, a.OUTPUT)

a.digitalWrite(LED, a.HIGH)

print 'reading sensor'
print 'value: ', a.analogRead(analog)
sleep(2)

a.digitalWrite(LED, a.LOW)
sleep(2)

print 'writing high'
a.analogWrite(LED, 200)
sleep(2)

print 'writing mid'
a.analogWrite(LED, 80)
sleep(2)

print 'writing low'
a.analogWrite(LED, 0)
sleep(2)

print 'Starting loop'


while (True):
  sensor_value =  a.analogRead(analog)
  brightness = sensor_value/1024.0 * 200
  a.analogWrite(LED, brightness)
  sleep(.1)



