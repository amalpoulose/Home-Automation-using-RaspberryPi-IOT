# Home-Automation-using-RaspberryPi-IOT

![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/smart-home.jpg)

# Introduction

Home automation or domotics is building automation for a home, called a smart home or smart house.ome automation gives you access to control devices in your home from a mobile device anywhere in the world. The term may be used for isolated programmable devices, like thermostats and sprinkler systems, but home automation more accurately describes homes in which nearly everything -- lights, appliances, electrical outlets, heating and cooling systems -- are hooked up to a remotely controllable network.Home automation is a step toward what is referred to as the "Internet of Things," in which everything has an assigned IP address, and can be monitored and accessed remotely.

Automation refers to the ability to program and schedule events for the devices on the network. The programming may include time-related commands, such as having your lights turn on or off at specific times each day. It can also include non-scheduled events, such as turning on all the lights in your home when your security system alarm is triggered.

The other main characteristic of cutting-edge home automation is remote monitoring and access.Monitoring apps can provide a wealth of information about your home, from the status of the current moment to a detailed history of what has happened up to now. You can check your security system's status, whether the lights are on, whether the doors are locked, what the current temperature of your home is and much more. With cameras as part of your home automation system, you can even pull up real-time video feeds and literally see what's going on in your home while you're away.

# prerequisites:

 Software : Python

     External modules needed
               Pubnub
               Twilio
               I2c tools
               Picamera
 Try the below commands to fullfill software requirements  :
 
      $chmod +x setup.sh
      $./setup.sh
 Hardware : 
 
    Raspberry Pi
    
    sensors : IR, LDR, RTC(DS3231), Temperature Sensor(DS18b20), PIR, Picamera, Relay, Buzzer
       
    

# Setting Up DS18B20

Before executing this program add below lines into /boot/config.txt
add below lines at the end of /boot/config.txt
and reboot your raspberry pi

    #enable ds18b20	
    dtoverlay=w1-gpio,gpiopin=5
    gpiopin numbering scheme is BCM pin number
 
 Temperature data will be available in file :
 
     vi /sys/bus/w1/devices/28-xxxxxxxxxxxxxxxxxxx/wi_slave

# Setting up I2c and Picamera

Run sudo raspi-config and choose in the menu to enable the pi camera and I2c

     $sudo raspi-config
     choose interfacig options
