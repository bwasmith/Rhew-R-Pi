#Environmental Sensor DataLogging using Raspberry Pi
By Brendan Smith and Dr. Julian Deventer  
Under Dr. Robert Rhew's Atmospheric Biogeochemistry lab at UC Berkeley    

_Please note:_  
This page is maintained by someone of intermediate technical expertise, please help contribute!  
Any questions please send to bsmithpolo at gmail dot com or post as Github [Issues](https://github.com/bwasmith/Rhew-R-Pi/issues)

##Overview 
Inspired by the Maker Movement and with the emergence of low cost technologies like Raspberry Pi and Arduino, there is opportunity for research communities to bypass high cost logging technologies provided by vendors. Lower cost alternatives exist via emerging technologies and with minimal expertise. 

This project walks through setting up devices, creating simple sensor readers, and storage of information.  

Much of the information provided was not created, it is merely a helpful aggregation of sample projects and data sheets to aid with re-creating a project or serve as a reference. 

Raspberry Pi code is written as Python scripts. 

##Directories
1. [Setting up the Raspberry Pi](https://github.com/bwasmith/Rhew-R-Pi/wiki/Setting-up-Raspberry-Pi)
2. [Getting started with GPIO](https://github.com/bwasmith/Rhew-R-Pi/wiki/Getting-started-with-GPIO)
3. Temperature and Humidity Sensing over I2C
4. Data Logging in Python
5. ADC with Rasp-pi
6. RhewLab Project
 
##Main Supplies  
####Hardware  
- Raspberry Pi 3
- Adafruit Breakout: [ADS1115 16-bit ADC](https://www.adafruit.com/product/1085)
- Adafruit Breakout: [DS1307 Real Time Clock](https://www.adafruit.com/products/264)

####Battery  
- EC Technology 22400mAh Power Bank  

####Sensors  
- Kipp and Zonen [PAR Quantum Sensor](http://www.kippzonen.com/Product/184/PQS-1-PAR-Quantum-Sensor)
- Adafruit Breakout: [SHT31-D Temperature and Humidity](https://www.adafruit.com/products/2857)
- Decagon [EC-5 Soil Moisture](https://www.decagon.com/en/soils/volumetric-water-content-sensors/ec-5-lowest-cost-vwc/)
