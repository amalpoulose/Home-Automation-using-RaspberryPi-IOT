# Home-Automation-using-RaspberryPi-IOT

![alt text](https://github.com/amalpoulose/Home-Automation-using-RaspberryPi-IOT/blob/master/smart-home.jpg)


# prerequisites:

 1.Python
 
 2.Pubnub
 
 3.Twilio
 
 4.I2c tools
 
 5.Picamera
 
 Try the below commands  :
 
      $chmod +x setup.sh
      $./setup.sh

# Setting Up DS18B20

Before executing this program add below lines into /boot/config.txt
add below lines at the end of /boot/config.txt
and reboot your raspberry pi

    #enable ds18b20	
    dtoverlay=w1-gpio,gpiopin=5
    gpiopin numbering scheme is BCM pin number
 
 Temperature data will be available in file :
 
 vi   /sys/bus/w1/devices/28-xxxxxxxxxxxxxxxxxxx/wi_slave
