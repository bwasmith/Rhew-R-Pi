#Connecting to ADC with Raspi

To collect information from sensors, [analog](https://learn.sparkfun.com/tutorials/analog-vs-digital) measurements need to be made.

The Raspberry Pi does not come with analog read capabilities by default, so an additional device is requred. Here we are using Adafruit's [ADS1015 12bit ADC](https://www.adafruit.com/products/1083?gclid=CjwKEAjwrIa9BRD5_dvqqazMrFESJACdv27GEaDDejUD2mtKzwyZ2VyJ3baQXLmWOLL-x1sPT6pCKxoC2aLw_wcB)

The idea is that the Raspberry Pi can use it's pins to communicate with other devices. So when we have something the Pi cannot do, an additional device can perform it for us. Then we just need to establish communication.

Raspberry Pi and the ADS1015 will communicate via the I2C(inter-integrated circuit) protocol, and is very easy to set up. 

##Enabling I2C on Raspi

Set up I2C on the Raspberry Pi with [this tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c).

##Using the ADS1x15

[This ADS1x15 setup link](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/assembly-and-wiring) will help you assemble the ADC chip. 

[This pinout diagram](https://developer.microsoft.com/en-us/windows/iot/win10/samples/pinmappingsrpi2) is very useful for finding the right pins on your Pi.

Adafruit has [this excellent tutorial](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115) for getting started with their device.


