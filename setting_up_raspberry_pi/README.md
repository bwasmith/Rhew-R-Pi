#Setting up Raspberry Pi

Great, now you have got a Raspberry Pi. Lets get it going. 

<img src="https://cdn2.peterdavehello.org/wp-content/uploads/2016/02/Raspberry-Pi-3-Model-B-Diagram-from-RS.png" height="475" width="660"><sup>[1]</sup>
##General Notes
A case on the Pi will prevent the metal pins on the bottom from resting on a conductive surface.

You will need a 5V power supply that can support ~2.5A of current. You can expect your Pi to take between 1-2A at all times depending on the computer's load. 

##Heat Sinks
[Here](https://www.flickr.com/photos/ultrapurple/16484032956) is an image of why you might want a heat sink. If you do not have them, you should be all right.

Make sure that you use thermal adhesive, and apply to heat sinks to CPU and Network/USB chip. 

##Installing the Operating System (Rasbian)
Raspbian is the [Linux](https://www.linux.com/what-is-linux) distribution recommended for our device. We will need it to use our computer.

You can purchase a SD card with Noobs installed, or you can follow [these instructions](https://www.raspberrypi.org/documentation/installation/noobs.md) to setup your own SD card. 

After, insert the SD card to the bottom of the Raspberry Pi, connect HDMI, a mouse, and a keyboard, then power it on. 

You should see:   
<img src=./sample_noobs.png width=500; height=370>


Continue through and your Raspberry Pi should be up and running.

##Basic Setup
Keyboard and local time needs to be set up following installation.

Open the terminal 

    sudo raspi-config

###Keyboard
Please see [**here**](https://thepihut.com/blogs/raspberry-pi-tutorials/25556740-changing-the-raspberry-pi-keyboard-layout) for full instructions and associated pictures

###Timezone and Clock
1. Navigate to "Internationalisation Options"
2. "Change Timezone"
3. Then select country and city


##Connecting to the internet
This was a headache for me, hopefully it will not be for you. 

Connecting is straightforward if you have a standard wired connection or "select network, enter password" Wifi (see: [WPA-Personal](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access#WPA_terminology)).

Things are more complicated if you have a static IP or are trying to connect on Airbears2. 

**_DO NOT_** change your **/etc/network/interfaces** file. Forum help for this is for older versions and should be unnecessary.

###Standard Connection
1. Click network button in top right corner
2. Select your network  
3. Enter password if necessary

###Ethernet with a Static IP address
You will need an IP address, a subnet mask, a router/gateway, a DNS server, and a domain.

1. _Right click_ network button in top right corner
2. Select "Wifi Network Settings"  
3. Configure -> "interface:eth0"
4. Enter information

Here is an example:  

<img src=./sample_ethernet_settings.png width="343" height="366">

_NOTE: If your subnet mask looks like: "255.255.255.xxx". we will need to convert to CIDR notation. Please use [this tool](http://www.subnet-calculator.com/cidr.php) and paste the CIDR notation address._

###WPA-Enterprise (Airbears2, UC Berkeley’s campus wifi)
Airbears2 poses a different challenge. To log in, a username and password is required.  
To connect, we will need to modify a network configuration file. The internet recommends to set up Wifi on an Android phone, and copy/paste the created configuration file. For convenience, I have included sample config file. 

Open the file with:

    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

And add the following:  

<img src=./annotated_wpa_supplicant.png width="500" height="271">

Double check your file, then "ctrl + X" to exit, "y" to save, "enter" to save.  

Restart your Pi to reload network changes.

##Once Connected to the Internet
Run 

    sudo apt-get update
And

    sudo apt-get -y upgrade

You can install any application  using 

    sudo apt-get install _______

####References
<sup>[1]</sup>[Raspberry Pi 3 diagram](http://docs-europe.electrocomponents.com/webdocs/14ba/0900766b814ba685.pdf) from [RS online Raspberry Pi 3 page](http://uk.rs-online.com/web/p/processor-microcontroller-development-kits/8968660/)
