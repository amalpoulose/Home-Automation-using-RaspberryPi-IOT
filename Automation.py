#! /usr/bin/python2.7 

import os
import i2c
import spi
import sys
import temp
import mail
import signal
import time
import picamera as cam
import RPi.GPIO as GPIO
from pubnub import Pubnub
from twilio.rest import Client
from multiprocessing import Process,Queue

#setting channel names for pubnub
channel1="Txt-data"
channel2="Rcv-data"

#Assigning Pin Numbers
BULB = 23
TAP=24
FAN = 16
MOTOR =20
PIR=21
WARNING=12

#Twilio initialization
client=Client("Axxxxxxxxxxxxxxxxxxxxxxa","exxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxb") 


def init():
       #uses Bradcom pin numbering scheme
	GPIO.setmode (GPIO.BCM)
	
       #remove all runtime warings in gpio 
	GPIO.setwarnings(False)

	GPIO.setup(BULB,GPIO.OUT) #setting up bulb pin
	GPIO.setup(FAN,GPIO.OUT)  #setting up fan pin
	GPIO.setup(TAP,GPIO.OUT)  #setting up Tap pin
	GPIO.setup(MOTOR,GPIO.OUT)#setting up motor pin
	GPIO.setup(PIR,GPIO.IN)#setting up PIR pin
	GPIO.setup(WARNING,GPIO.OUT)#setting up PIR pin

        #connecting in active low so turn off 
	GPIO.output(BULB,True) 
	GPIO.output(FAN,True)
	GPIO.output(MOTOR,True)
	GPIO.output(TAP,True)
	GPIO.output(WARNING,True)

        #change default action of SIGCHLD
	signal.signal(signal.SIGCHLD,handler1)

	pubnub = Pubnub(publish_key='pub-cxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3', subscribe_key='sub-cxxxxxxxxxxxxxxxxxxxxxxxxxx1')
	#initialize adc
	spi.adc_setup()
	return pubnub

def callback(m): #publishing status
	print(m)

def __callback__(m, channel):    #subscribing status
	if 'bulb' in m :
		if m['bulb'] == 1:
			    GPIO.output(BULB,False)
			    print "bulb on"
		else:
			    GPIO.output(BULB,True)
			    print "bulb off"
	if 'fan' in m:
		if m['fan'] == 1:
			    GPIO.output(FAN,False)
			    print "fan on"
		else:
			    GPIO.output(FAN,True)
			    print "fan off"
	if 'motor' in m:
		if m['motor'] == 1:
			    GPIO.output(MOTOR,False)
			    print "motor on"
		else:
			    GPIO.output(MOTOR,True)
			    print "motor off"
		

def __error__(m):  #error while subscribing
	print(m)

def handler1(signum,frame): #Action performed for SIGCHLD signal
	try:
		os.wait()
		print "child exited"
	except OSError:
		pass


def main():

	pubnub=init()
	pubnub.subscribe(channels=channel2, callback=__callback__, error=__error__)


      # Automation using LDR to turn on and turn off light
	def ldr():
     		bulb_flg=0
      		while(1):
        		time.sleep(2)
      		      #reading RTC value
			t=i2c.i2c_time()
        		os.system("clear")
			print "Time : ",t
       #reading LDR value
			LDR=spi.adc_read(0)
			print "LDR : ",LDR
			if LDR>3600 and bulb_flg==0:
	   			time.sleep(3)
	   			LDR=spi.adc_read(0)
	   			if LDR>3600: 
					data = {
        					'BULB':'ON'
						}	
					pubnub.publish(channel1, data, callback=callback, error=callback)
	        			GPIO.output(BULB,False)
					message=client.messages.create(
									to="+919446047003",
									from_="+14xxxxxxxx2",
									body="Light is turning on at "+t)
					print message.sid
	        			bulb_flg=1
			elif LDR<=3600 and bulb_flg==1:
	       				GPIO.output(BULB,True)
					bulb_flg=0


      # Automation using IR to turn on and off Tap
  	def ir():
    		while(1):
      		       #reading RTC value
        		time.sleep(2)
			t=i2c.i2c_time()
        		os.system("clear")
			print "Time : ",t
    		       #reading IR value 
			IR=spi.adc_read(1)
			print "IR : ",IR
			if IR<3000 :
	        		GPIO.output(TAP,False)
				time.sleep(3)
	        		GPIO.output(TAP,True)


      # Automation using DS18b0 to turn on and turn off ac/fan
  	def temper():
    		fan_flg=0
     		while(1):
       			time.sleep(2)
                       #reading RTC value
			t=i2c.i2c_time()
        		os.system("clear")
			print "Time : ",t
                       #reading temperature value
			tem=temp.read_temp()
			print "Temperature : ",tem," c"
       
			if tem>29.0 and fan_flg==0:
	   			time.sleep(3)
	   			tem=temp.read_temp()
	   			if tem>29.0: 
					data = {
        					'FAN':'ON'
						}	
					pubnub.publish(channel1, data, callback=callback, error=callback)
	      				GPIO.output(FAN,False)
					message=client.messages.create(
							to="+919446047003",
							from_="+14xxxxxxx2",
							body="AC is turning on at "+t+"\ntemperature : "+str(tem) )
					print message.sid
	        			fan_flg=1
			elif tem <=29.0 and fan_flg==1:
	        		GPIO.output(FAN,True)
				fan_flg=0


       #Theft detection using PIR
	def pir():
		
     		while(1):
                       #reading RTC value
			t=i2c.i2c_time()
       			os.system("clear")
			print "Time : ",t
			if GPIO.input(PIR):
	        		print "Security alert"
				data = {
        				'Security':'Alert'
					}	
				pubnub.publish(channel1, data, callback=callback, error=callback)
				c=cam.PiCamera()
				c.capture("img.jpg")
				c.close()
	        		GPIO.output(WARNING,False)
				message=client.messages.create(
						to="+919446047003",
						from_="+14xxxxxxxx2",
						body="Some one at Home \n\nTime: "+t )
				s=mail.my_mail("gmail username","password")
				s.send_mail("amalpoulose1995@gmail.com","Attention:Security Issue","Some one in your home","./img.jpg")

				time.sleep(10)
	        		GPIO.output(WARNING,True)
                	time.sleep(2)

        #creating subprocesses
  	p1=Process(target=ldr)
 	p2=Process(target=ir)
  	p3=Process(target=temper)
  	p4=Process(target=pir)
	#starting all subprocesses
  	p1.start()
  	p2.start()
  	p3.start()
  	p4.start()

#boilerplate syntax
if __name__ == "__main__":
	main()
