# Home-Automation-using-RaspberryPi-IOT

![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/smart-home.jpg)

# Introduction

Home automation or domotics is building automation for a home, called a smart home or smart house.Home automation gives you access to control devices in your home from a mobile device anywhere in the world. The term may be used for isolated programmable devices, like thermostats and sprinkler systems, but home automation more accurately describes homes in which nearly everything -- lights, appliances, electrical outlets, heating and cooling systems -- are hooked up to a remotely controllable network. Home automation is a step toward what is referred to as the "Internet of Things," in which everything has an assigned IP address, and can be monitored and accessed remotely.

Automation refers to the ability to program and schedule events for the devices on the network. The programming may include time-related commands, such as having your lights turn on or off at specific times each day. It can also include non-scheduled events, such as turning on all the lights in your home when your security system alarm is triggered.

The other main characteristic of cutting-edge home automation is remote monitoring and access.Monitoring apps can provide a wealth of information about your home, from the status of the current moment to a detailed history of what has happened up to now. You can check your security system's status, whether the lights are on, whether the doors are locked, what the current temperature of your home is and much more. With cameras as part of your home automation system, you can even pull up real-time video feeds and literally see what's going on in your home while you're away.

# prerequisites:

 Software :
 
     Python2.7
          External python modules needed :
               -> Pubnub
               -> Twilio
               -> I2c tools for smbus
               -> Picamera
 Try the below commands to fulfill software requirements  :
 
      $chmod +x setup.sh
      $./setup.sh

Hardware : 

    Raspberry Pi
    
    sensors : IR, LDR, RTC(DS3231), Temperature Sensor(DS18b20), PIR, Picamera, Relay, Buzzer
       
    

# Setting Up DS18B20(Temperature Sensor)

Before executing this program add below lines into /boot/config.txt
add below lines at the end of /boot/config.txt
and reboot your raspberry pi

    #To enable ds18b20	
    dtoverlay=w1-gpio,gpiopin=5
    
 Connect temperature sensor output to BCM5
 
 Temperature data will be available in file :
 
     vi /sys/bus/w1/devices/28-xxxxxxxxxxxxxxxxxxx/wi_slave

# Setting up I2C and Picamera

Run sudo raspi-config and choose in the menu to enable the pi camera and I2c

     $sudo raspi-config
     choose interfacig options
     enable i2c
     enable picamera
     
# RaspberryPi 3B 

![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/raspberrypi.jpg)

Features:

    1.CPU: Quad-core 64-bit ARM Cortex A53 clocked at 1.2 GHz
    2.GPU: 400MHz VideoCore IV multimedia
    3.Memory: 1GB LPDDR2-900 SDRAM (i.e. 900MHz)
    4.USB ports: 4
    5.Video outputs: HDMI, composite video (PAL and NTSC) via 3.5 mm jack
    6.Network: 10/100Mbps Ethernet and 802.11n Wireless LAN
    7.Peripherals: 17 GPIO plus specific functions, and HAT ID bus
    8.Bluetooth: 4.1
    9.Power source: 5 V via MicroUSB or GPIO header 
    10.Size: 85.60mm × 56.5mm
    11.Weight: 45g (1.6 oz)
 

 # Pin Connections
 
![alt text](https://pinout.xyz/resources/raspberry-pi-pinout.png)

    -> DS3231 :
      --------
          RTC   :   RaspberryPi
        ------     -------------
          SDA           SDA(BCM2)
          SCL           SCL(BCM3)
          
    -> MCP3204 :
      ---------
          ADC    :    RaspberryPi
         -----       -------------
          clk           BCM22
          cs            BCM27
          din           BCM17
          dout          BCM18
     
    -> LDR :
      -----
        A0  : ch0 of Mcp3204
     
    -> IR :
      ------
        A0 : ch1 of Mcp3204
     
    -> DS18b20 :
      ---------  
        out  : BCM 5 of RaspberryPi
    
    -> PIR :
      -----
        out  : BCM21 of RaspberryPi
    
    -> Refer output pins from program 
    -> Connect picamera to camera slot
    
# Instructions to run the code

      1. Run following command to install all required Libraries
      
           chmod +x setup.sh
           ./setup.sh
      
      2. All file should be in same folder especially i2c.py, spi.py, temp.py, mail.py
      3. Create account on pubnub(https://www.pubnub.com/) 
      4. Use the publish and subscribe keys in Program 
      5. Create account on Twilio(https://www.twilio.com/)
      6. Use account sid and Auth Token in program 
      7. Create your twilio number(+1415xxxxxx) and include it in the program
      8. Add mail id and password from which you want to send also add destination mail id
      9. Do steps to setup Temperature sensor DS18B20(refer above).
     10. Do steps to enable I2C & Picamera(refer above). 
     11. Use Automation.py to run the project.While testing check your mobile and mailbox
     12. Use pubnub_txt.py for controlling the system using pubnub
     13. Use pubnub_rcv.py for view the messages recieved in pubnub
     
![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/circuit-breadboard-1.jpg)
![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/circuit-breadboard-2.jpg)
