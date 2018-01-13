#!/usr/bin/python2.7

import os
import sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-xxxxxxxxxxxxxxxxxxxxxxxxxxxx3', subscribe_key='sub-c-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1')
channel = "Rcv-data"
def callback(m):
	print m

def main():
	while True:
		os.system("clear")
		print "1. Bulb on"
		print "2. Bulb off"
		print "3. Fan/Ac on"
		print "4. Fan/Ac off"
		print "5. Motor on"
		print "6. Motor off"
		choice=input("choice? : ")
		if choice==1:
			data={"bulb":1}
			pubnub.publish(channel,data,callback=callback,error=callback)
		elif choice==2:
			data={"bulb":0}
			pubnub.publish(channel,data,callback=callback,error=callback)
		elif choice==3:
			data={"fan":1}
			pubnub.publish(channel,data,callback=callback,error=callback)
		elif choice==4:
			data={"fan":0}
			pubnub.publish(channel,data,callback=callback,error=callback)
		elif choice==5:
			data={"motor":1}
			pubnub.publish(channel,data,callback=callback,error=callback)
		elif choice==6:
			data={"motor":0}
			pubnub.publish(channel,data,callback=callback,error=callback)
		else:
			print "\nInvalid Choice"
		
	
if __name__=="__main__":
	main()	
