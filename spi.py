#! /usr/bin/python2.7
import RPi.GPIO as gpio
import time
import os
import i2c
mosi=17
miso=18
cs =27
scl=22

def adc_setup():
	'''syntax : spi.adc_setup() 
	   Initialize the spi 
	   MOSI(17),MISO(18),CS(27),SCL(22)'''
	#Set the BCM pin number scheme
	gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
	#set mosi , miso ,cs ,scl line 
	gpio.setup(mosi,gpio.OUT)
	gpio.setup(miso,gpio.IN)
	gpio.setup(cs,gpio.OUT)
	gpio.setup(scl,gpio.OUT)
	

def adc_read(channel=0):
	'''syntax : spi.adc_read(channelNo)->adc_value
	   It is used to read the adc values'''
	# chip select 0
	gpio.output(cs,False)

	# start bit
	gpio.output(scl,False)
	gpio.output(mosi,True)
	gpio.output(scl,True)
	
	# single/diff bit
	gpio.output(scl,False)
	gpio.output(mosi,True)
	gpio.output(scl,True)
	
	# d2 bit don"t care
	gpio.output(scl,False)
	gpio.output(mosi,True)
	gpio.output(scl,True)
	
	# d1 bit
	gpio.output(scl,False)
	gpio.output(mosi,channel>>1)
	gpio.output(scl,True)
	
	# d2 bit
	gpio.output(scl,False)
	gpio.output(mosi,channel&1)
	gpio.output(scl,True)
	
	# Tsample bit
	gpio.output(scl,False)
	gpio.output(mosi,True)
	gpio.output(scl,True)
	
	# Null bit
	gpio.output(scl,False)
	gpio.output(mosi,True)
	gpio.output(scl,True)
	
	data=0
	#read the 12 bit data from ADC
	for i in range(11,-1,-1):
		gpio.output(scl,False)
		if gpio.input(miso) :
			data |= (1<<i)
		gpio.output(scl,True)
	gpio.output(cs,True)
	return data
		
