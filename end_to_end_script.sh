#!/usr/bin/env python

<<COMMENT1
  This is an end to end script connecting the RaspberryPi to Arduino and Environmental Sensors.
COMMENT1

from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep

ANALOG = 14
LED = 13
GAIN = 510.0
PAR_SENSITIVITY = 0.00000457
NUM_READS = 50

connection = SerialManager(device='/dev/ttyACM0')
arduino = ArduinoApi(connection=connection)
arduino.pinMode(LED, arduino.OUTPUT)

print "Starting up Pyranometer sensor read from Arduino"
print "Readings every 2 seconds..."

while (True):
  arduino.digitalWrite(LED, a.HIGH)
  
  for i in range(NUM_READS):
    sum += arduino.analogRead(ANALOG)
    sleep(.01)
  
  arduino.digitalWrite(LED, a.LOW)

  avg_analog_read = arduino.analogRead(ANALOG) / NUM_READS
  print "avg_analog_read: ", avg_analog_read
  
  volts = analog_read * 5.0 / 1024.0
  print "volts: ", volts

  original_signal = volts / GAIN
  print "original_signal: ", original signal
  
  irridance = original_signal / PAR_SENSITIVTY
  print "irridance: ", irridance
  
  sleep(2)

