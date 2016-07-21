#!/usr/bin/env python

#End to end script connecting the RaspberryPi to Arduino and Environmental Sensors.
#Information is routed from PAR sensor, through Arduino, to Pi
#Nanpy to connect to Arduino

#prints PAR reading every 2 seconds from 1/2 second avg analog read.

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
  arduino.digitalWrite(LED, arduino.HIGH)
  sum_reads = 0
  
  for i in range(NUM_READS):
    sum_reads += arduino.analogRead(ANALOG)
    sleep(.01)
  
  arduino.digitalWrite(LED, arduino.LOW)

  avg_analog_read = sum_reads / NUM_READS
  print "avg_analog_read: ", avg_analog_read
  
  volts = avg_analog_read * 5.0 / 1023.0
  print "volts: ", volts

  original_signal = volts / GAIN
  print "original_signal: ", original_signal
  
  irridance = original_signal / PAR_SENSITIVITY
  print "irridance: ", irridance
  
  sleep(2)

