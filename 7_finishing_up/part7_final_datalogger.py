'''
Environmental sensor datalogger for low cost sensing in Robert Rhew's Trace gas Biogeochemistry lab at UC Berkeley

Intended to be run on a Raspberry Pi with different sensors connected. Writes to a new or existing CSV file in the DATA_PATH directory. Logs every DELAY_INTERVAL period.

Dependencies for sensors:
- Adafruit_DHT
- Adafruit_ADS1x15.
'''

from time import sleep
import math
import csv
import os.path
from datetime import datetime
from gpiozero import LED

#import sensors
import Adafruit_DHT
import Adafruit_ADS1x15

#LOCAL VARIABLES
DATA_PATH = '/home/pi/Documents/env_datalogs' #data directory path
DATA_NAME = 'dht_logs' #data file name

now = datetime.now() #todays date
date_string = now.date().strftime("%Y_%m_%d")

DELAY_INTERVAL = 5

led = LED(17) #Blue wire, designated for LED
led_on = False

#Sensor Variables
dht_sensor = Adafruit_DHT.DHT22
DHT_PIN = 4

adc = Adafruit_ADS1x15.ADS1115()
ADC_GAIN = 16 #1->16, powers of 2. programmable gain, see datasheet for more info
POTENTIOMETER_ADC_PIN = 3

#Helper function to convert ADC output back into original voltage signal
def steps_to_millivolts(adc_output, volt_range, gain, num_steps):
  volts_per_step = volt_range * (1.0 / gain) * (1.0 / num_steps)
  millivolt_equivalent = adc_output * volts_per_step
  return millivolt_equivalent

#create total file path (with date)
file_name = DATA_PATH + '/' + date_string + '_' + DATA_NAME

#if the file does not already exist, create a new file with csv headers
if not os.path.isfile(file_name):
    csv_headers = ['Date', 'Time','Temperature', 'Humidity', 'Potentiometer mV']
    with open(file_name, 'w') as new_data_file:
        datawriter = csv.writer(new_data_file)
        datawriter.writerow(csv_headers)

#main logging sequence
while True:
    new_log = []

    now = datetime.now()
    date_string = now.date().strftime("%Y_%m_%d")
    time_string = now.time().strftime("%H:%M:%S")
    
    new_log.append(date_string)
    new_log.append(time_string)

    #sensor1 
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, DHT_PIN)
    new_log.append("{:0.1f}".format(temperature))
    new_log.append("{:0.1f}".format(humidity))
    
    #sensor2
    potentiometer_output = adc.read_adc(POTENTIOMETER_ADC_PIN, ADC_GAIN)
    potentiometer_millivolts = steps_to_millivolts(potentiometer_output, 4.096, ADC_GAIN, math.pow(2, 15))
    new_log.append("{:0.6f}".format(potentiometer_millivolts))
    
    #write results to log
    with open(file_name, 'a') as data_log:
        logwriter = csv.writer(data_log)
        logwriter.writerow(new_log)
    print "Wrote Log: ", new_log

    #split DELAY_INTERVAL into many 1 second intervals
    #toggle the led every second
    for i in range(DELAY_INTERVAL):
        if led_on:
            led.off()
            led_on = False
        else:
            led.on()
            led_on = True
        
        sleep(1)
