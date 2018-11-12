# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:51:16 2018

@author: reddy
"""

import re
ip=[]

iplst=[]
validip=[]
invalidip=[]
logdat=[]
logout=[]
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
date= '\d{2}:\d{2}:\d{2}'
with open("authlog.txt") as txt:
	for row in txt:
		if "Accepted publickey"in row:
			
			lst=row.split(" ")
			for line in lst:				
				finalIP = re.findall(pattern,line)
				logdate=re.findall(date,line)
				iplst.append(finalIP)
				iplst = [x for x in iplst if x]
				logdat.append(logdate)
				logdat = [x for x in logdat if x]




		if "Disconnected" in row:

			ip=re.findall(pattern,row)
			if(ip in iplst):
				print("valid logout",ip[0])
				logoutt=re.findall(date,row)
				validip.append(ip)
				logout.append(logoutt)
			else:
				#print(ip,"Invalid ")
				invalidip.append(ip)

	print("total ip list:",len(iplst))
	
	print("login time",len(logdat))
	print("total valid logouts:",len(validip))
	print("Logout time:",len(logout))
	print(logdat[0])
	print(logout[0])
	print("total invalid list:",len(invalidip))

rsaa=[]
rss={}
with open("authlog.txt",'r') as txt:
	for row in txt:
		if "Accepted publickey"in row:
			lst=row.split(" ")
			rsa = re.findall(r'RSA.*',row)
			if rsa not in rsaa:
				rss[rsa[0]]=1;
				rsaa.append(rsa)
			else:
				rss[rsa[0]]+=1
	print("Individual users RSA")
	print(rss)		