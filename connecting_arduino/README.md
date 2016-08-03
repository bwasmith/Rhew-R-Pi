#Connecting Arduino with Raspi

To collect information from sensors, [analog](https://learn.sparkfun.com/tutorials/analog-vs-digital) measurements need to be made. 

The Rapsberry Pi does not come with analog read capabilities by default, so an additional device is required. [Arduino](https://www.arduino.cc/) is a very popular, community supported device that is easy to connect with the Raspberry Pi. 

The relationship between the two follows a "master-slave" example, where the Raspberry Pi is the controller and the Arduino is the controlled.  

For these instructions, you should go through the [Arduino Getting Started](https://www.arduino.cc/en/Guide/HomePage) and also the [Analog Input Tutorial](https://www.arduino.cc/en/Tutorial/AnalogInput)

##Nanpy
To establish communication, a library called Nanpy is both installed on your Raspberry Pi and uploaded onto the Arduino. Then, the two will be connected via usb.

Please visit the [Nanpy Python Website](https://pypi.python.org/pypi/nanpy), their instructions are clear and are my source of knowledge.

###Raspberry Pi Nanpy
Simple,   

     sudo pip install nanpy  

Easy money. Now you can import the ArduinoAPI from a Python script.

###Arduino Nanpy
If you have not already installed the Arduino IDE, please do so now.  

Get the Nanpy directories:

     git clone https://github.com/nanpy/nanpy-firmware.git
     cd nanpy-firmware
     ./configure.sh

Copy Nanpy directory to our Arduino Sketchbook

    cp -r ~/nanpy-firmware/Nanpy ~/sketchbook

Restart the Arduino IDE, File --> Sketchbook --> Nanpy. Upload the contents.

_Note: I had trouble uploading from the Raspberry Pi. So, I uploaded Nanpy to the Arduino from my Mac, then connected the Pi and Arduino._

##An Example Analog Read via Python Script

Follow the Arduino [Analog Input](https://www.arduino.cc/en/Tutorial/AnalogInput) tutorial, and see the [refashioned code](https://github.com/bwasmith/Rhew-R-Pi/tree/master/connecting_arduino/nanpy_analog_input.sh) for a Raspberry Pi Python script. 

Copy/paste the script into a new editor, 
Add excecutable permissions:

    sudo chmod +x nanpy_analogread.sh

Run the script:

    ./nanpy_analogread.sh

I also included another sample script which calls Arduino's PWM [AnalogWrite](https://www.arduino.cc/en/Reference/AnalogWrite).

##Helpful Notes

- Arduino Analog Input pins 0-6 are referenced as pins #14-20
