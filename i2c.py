#!/usr/bin/python2.7

import smbus
import time
import sys
def init():
        ''' Initialize i2c 
	    I2C1 is used in this module'''
	try:
		bus=smbus.SMBus(1)#1 = /dev/i2c-1 (port I2C1)
		#returns struct_time
		t=time.strptime(time.ctime())

		#store bcd of seconds minute and hour
        	sec=int(str(t[5]),16)
        	m=int(str(t[4]),16)
        	hr=int(str(t[3]),16)
		#store time data to RTC register
		bus.write_byte_data(0x68,0x00,sec)
		bus.write_byte_data(0x68,0x01,m)
		bus.write_byte_data(0x68,0x02,hr)
		return bus
	except IOError:  #If rtc is not connected
		print "No RTC Found"
		sys.exit(-1)
def i2c_time():
                '''syntax : i2c.i2c_time()-
		   returns current time in 24 hour format'''
		bus=init()
		# Read time from the RTC register
		hr=bus.read_byte_data(0x68,0x2)
		m =bus.read_byte_data(0x68,0x1)
		s =bus.read_byte_data(0x68,0x0)
		#return string of time	
		return str(hex(hr)[2:])+":"+str(hex(m)[2:])+":"+str(hex(s)[2:])
