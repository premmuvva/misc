# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:27:13 2018

@author: reddy
"""

def main():
    s=input()
    length=len(s)
    d=dict()
    for i in range (26):
        d[chr(i+ord('a'))]=0
    for i in range (length):
        if(s[i]>='a' and s[i]<='z'):
            d[s[i]]+=1
            if(d[s[i]]%2!=0):
                print(s[i],end="")
        elif(s[i]>='A' and s[i]<='Z'):
            d[chr(ord(s[i])-chr('A')+chr('a'))]+=1
            if(d[chr(ord(s[i])-chr('A')+chr('a'))]%2!=0):
                print(s[i],end="")
        else:
            print (s[i],end="")
main()