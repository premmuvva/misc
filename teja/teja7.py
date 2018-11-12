# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 00:26:48 2018

@author: reddy
"""
import re
ip = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
login= '\d{2}:\d{2}:\d{2}'   
valid=dict() 
invalid=0
def main():
    global invalid 
    with open("authlog.txt") as txt:
        for row in txt:
            if "Accepted publickey"in row:
                if re.findall(ip,row)[0] in valid.keys() : 
                    valid[re.findall(ip,row)[0]].append([1,re.findall(r'RSA.*',row)[0],re.findall(login,row)[0]])
                else:
                    valid[re.findall(ip,row)[0]]=[0,[1,re.findall(r'RSA.*',row)[0],re.findall(login,row)[0]]]
            elif "Received disconnect" in row:
                if "error:" in row:
                    continue
                if (re.findall(ip,row)[0] in valid.keys()) :
                    if len(valid[re.findall(ip,row)[0]])>1 and (valid[re.findall(ip,row)[0]][len(valid[re.findall(ip,row)[0]])-1][0]) == 1 :
                            valid[re.findall(ip,row)[0]][len(valid[re.findall(ip,row)[0]])-1][0]=0
                            valid[re.findall(ip,row)[0]][len(valid[re.findall(ip,row)[0]])-1].append(re.findall(login,row)[0])
                    else:
                        valid[re.findall(ip,row)[0]][0]+=1
                else :
                    valid[re.findall(ip,row)[0]]=[1]
    for ips in valid.keys() :
        invalid += (valid[ips][0])
                #valid[re.findall(ip,row)].append()
                    
main()
print(valid)
count=0
for txt in valid.keys():
    for nxt in valid[txt]:
        if type(nxt) is list :
            if nxt[0]==0:
                count+=1
print (count)
print (invalid)