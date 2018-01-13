#! /usr/bin/python2.7

import time
import sys
import os
from pubnub import Pubnub


CH_CHANNEL="Txt-data"

def init(ch):
	pubnub = Pubnub(publish_key='pub-c-xxxxxxxxxxxxxxxxxxxxxxxxxxx3', subscribe_key='sub-c-xxxxxxxxxxxxxxxxxxxxxxxxx1')
	channel = ch
	return (pubnub,channel)

def __callback__(m, channel):
	os.system("clear")
	for i in m.keys():
		print i," : ",m[i]
#	time.sleep(1)
def __error__(m):
	print(m)
 
def main():
	(pubnub,channel)=init(CH_CHANNEL)
	pubnub.subscribe(channels=channel, callback=__callback__, error=__error__)

if __name__ == "__main__":
	main()
