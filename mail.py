#!/usr/bin/python2.7
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class my_mail:
	def __init__(self,name,passwd):
		self.server=smtplib.SMTP('smtp.gmail.com',587) # for port number 465 use smtplib.SMTP_SSL('smtp.gmail.com',465)
        	self.usrname=name
		self.password=passwd
	

	def send_mail(self,To,sub,body,image):
		#open image in read binary mode and read the data
    		img_data = open(image, 'rb').read()
		From=self.usrname+"@gmail.com"
		#message format
    		msg = MIMEMultipart()
    		msg['Subject'] = sub
    		msg['From'] = From
    		msg['To'] = To
    		text = MIMEText(sub)
    		msg.attach(text)
    		image = MIMEImage(img_data, name=os.path.basename(image))
    		msg.attach(image)
    		#self.server.ehlo()#when using port 465
    		self.server.starttls()
    		self.server.login(self.usrname,self.password)
    		self.server.sendmail(From, To, msg.as_string())
   		self.server.close()

