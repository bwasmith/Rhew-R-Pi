from time import sleep
import math
import csv
import os.path

#import datetime
from datetime import datetime

#import sensors
import Adafruit_DHT
import Adafruit_ADS1x15

#LOCAL VARIABLES
#data directory path
data_path = '/home/pi/Documents/env_datalogs'
#data file name
data_name = 'dht_logs'
#todays date
now = datetime.now()
date_string = now.date().strftime("%Y_%m_%d")
#sensor list
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4

adc = Adafruit_ADS1x15.ADS1115()
adc_gain = 16 #1->16, powers of 2. programmable gain, see datasheet for more info
potentiometer_adc_pin = 3

def steps_to_millivolts(adc_output, volt_range, gain, num_steps):
  volts_per_step = volt_range * (1.0 / gain) * (1.0 / num_steps)
  millivolt_equivalent = adc_output * volts_per_step
  return millivolt_equivalent


#create total file path (with date)
file_name = data_path + '/' + date_string + '_' + data_name

#if the file does not already exist, create a new file with headers
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
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    new_log.append(temperature)
    new_log.append(humidity)
    
    #sensor2
    potentiometer_output = adc.read_adc(potentiometer_adc_pin, adc_gain)
    millivolts = steps_to_millivolts(potentiometer_output, 4.096, adc_gain, math.pow(2, 15))
    new_log.append(millivolts)
    
    #write results to log
    with open(file_name, 'a') as data_log:
        logwriter = csv.writer(data_log)
        logwriter.writerow(new_log)
    print "Wrote Log: ", new_log
    sleep (5)
