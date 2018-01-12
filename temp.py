#!/usr/bin/python2.7
import os
def read_temp():
	path="/sys/bus/w1/devices/"
	#returns a list of directories
        sub=os.listdir(path)
	#finds the directory name start with 28 if not found raise exception
	for i in sub:
		if i[:2]=='28':
			break
	else: 
		raise Exception('Temperature Sensor Not Connected')
	#create path to file w1_slave
	path=os.path.join(path,i)
	path=os.path.join(path,"w1_slave")
	#open file w1_slave
	f=open(path,"rU")
	f.seek(0,0)
	#read contents to string
	s=f.read()
	#create a list of words of file
	l=s.split()
	f.close()
	#convert temperature to float and returns
	return float(l[-1][2:])/1000
