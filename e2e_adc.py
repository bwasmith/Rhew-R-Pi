from time import sleep
import math

import Adafruit_ADS1x15
import Adafruit_DHT

'''
This is an end to end communication channel of the Raspberry Pi with the Adafruit's ADS1015 ***12-bit*** ADC. 

Environmental sensors used are the: 

DHT22
  -> Digital communication directly with Pi
Kipp and Zonen PAR sensor
  -> Millivolt output read by ADC
'''
#static variable
GAIN = 16
PAR_SENSITIVITY = 0.00000457
COLLECTION_INTERVAL = 2

PAR_PIN = 0
DHT_PIN = 22

#setup
dht = Adafruit_DHT.DHT22

adc = Adafruit_ADS1x15.ADS1015()
ADC_SENSITIVITY = math.pow(2,11)

#adc = Adafruit_ADS1x15.ADS1115()
#ADC_SENSITIVITY = math.pow(2,15)


print "Starting reads from PAR sensor"
print 'Reading every {:d} seconds...'.format(COLLECTION_INTERVAL)

while True:
  par_readout = adc.read_adc(PAR_PIN, gain=GAIN)
  print "par_readout: {:d}".format(par_readout)

  #we turn a digital read back to a voltage
  adc_voltage_range = 4.096 / GAIN
  par_voltage = par_readout * (adc_voltage_range / ADC_SENSITIVITY)
  print "par_voltage {:0.1f}".format( par_voltage)

  irridance = par_voltage / PAR_SENSITIVITY 
  print "IRRIDANCE: {:0.1f}".format(irridance)

  humidity, temperature = Adafruit_DHT.read_retry(dht, DHT_PIN)
  print 'Temperature: {:0.1f}*C, Humidity: {:0.1f}%'.format(temperature, humidity)

  sleep(COLLECTION_INTERVAL)

