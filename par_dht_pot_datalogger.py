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
data_path = '/home/pi/Documents/env_datalogs' #data directory path
data_name = 'dht_logs' #data file name

now = datetime.now() #todays date
date_string = now.date().strftime("%Y_%m_%d")

DELAY_INTERVAL = 5

led = LED(17) #GPIO pin 17 for LED
led_on = False

#Sensor Variables
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4

adc = Adafruit_ADS1x15.ADS1115()
adc_gain = 16 #1->16, powers of 2. programmable gain, see datasheet for more info
potentiometer_adc_pin = 3 #pin A3

PAR_SENSITIVITY = 0.00000457
PAR_ADC_PIN = 0 #pin A0

#Helper function to convert ADC output back into original voltage signal
def steps_to_millivolts(adc_output, volt_range, gain, num_steps):
  volts_per_step = volt_range * (1.0 / gain) * (1.0 / num_steps)
  millivolt_equivalent = adc_output * volts_per_step
  return millivolt_equivalent

#create total file path (with date)
file_name = data_path + '/' + date_string + '_' + data_name

#if the file does not already exist, create a new file with csv headers
if not os.path.isfile(file_name):
    csv_headers = ['Date', 'Time','Temperature', 'Humidity', 'Potentiometer mV', 'PAR irridance']
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
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    new_log.append("{:0.1f}".format(temperature))
    new_log.append("{:0.1f}".format(humidity))
    
    #sensor2
    potentiometer_output = adc.read_adc(potentiometer_adc_pin, adc_gain)
    potentiometer_millivolts = steps_to_millivolts(potentiometer_output, 4.096, adc_gain, math.pow(2, 15))
    new_log.append("{:0.6f}".format(potentiometer_millivolts))
    
    #sensor3
    par_output = adc.read_adc(PAR_ADC_PIN, adc_gain)
    par_millivolts = steps_to_millivolts(par_output, 4.096, adc_gain, math.pow(2,15))
    irridance = par_millivolts / PAR_SENSITIVITY
    new_log.append("{:0.2f}".format(irridance))

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
