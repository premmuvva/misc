# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:48:33 2018

@author: reddy
"""

def encode(inp):
    out=""
    for i in range (0,len(inp),4) :
        intermediate=""
        temp=0
        for j in range (4):
            if ' '==inp[i+j]:#a-z 0-25 ; A-Z 26-51 ; ' ' 52 ; 0-9 53-62
                temp= 52
            elif (ord('a')<=ord(inp[i+j]) and ord(inp[i+j])<=ord('z')):
                temp=ord(inp[i+j])-ord('a')
            elif (ord('A')<=ord(inp[i+j]) and ord(inp[i+j])<=ord('Z')):
                temp=ord(inp[i+j])-ord('A')+26
            elif (ord('0')<=ord(inp[i+j]) and ord(inp[i+j])<=ord('9')):
                temp=ord(inp[i+j])-ord('0')+53
            #print(temp)
            intermediate+=chr(temp)
        out+=chr((ord(intermediate[0])*4+int(ord(intermediate[1])/16))%(2**8))+chr(((ord(intermediate[1])*16)%(2**8)+int(ord(intermediate[2])/4))%(2**8))+chr((ord(intermediate[2])*64+ord(intermediate[3]))%(2**8))
    #print(out,len(out),sep="",end="")
    return out
        
def decode(inpu):
    out=''
    for i in range (0,len(inpu),3) :
        intermediate=chr(int(ord(inpu[i])/4))+chr(int(((ord(inpu[i])*64)%(2**8))/4)+int(ord(inpu[i+1])/16))+chr(int(((ord(inpu[i+1])*16)%(2**8))/4)+int(ord(inpu[i+2])/64))+chr(int(((ord(inpu[i+2])*4)%(2**8))/4))       
        for j in range (4):
            if 52==ord(intermediate[j]):#a-z 0-25 ; A-Z 26-51 ; ' ' 52 ; 0-9 53-62
                out+= ' '
            elif (0<=ord(intermediate[j]) and ord(intermediate[j])<=25):
                out+=chr(ord(intermediate[j])+ord('a'))
            elif (26<=ord(intermediate[j]) and ord(intermediate[j])<=51):
                out+=chr(ord(intermediate[j])+ord('A')-26)
            elif (53<=ord(intermediate[j]) and ord(intermediate[j])<=62):
                out+=chr(ord(intermediate[j])+ord('0')-53)
    #print(out,sep="",end="")
    return out
def main():
    txt=open("in.txt",'r')
    txt1=open("out.txt",'w')
    print("encode : " )
    for line in txt:
        for i in range (0,len(line)-4,4):
            txt1.write(encode(line[i:i+4]))
        i+=4
        
        if (len(line)%4!=0):
            line+=(4-len(line)%4)*' '
        txt1.write(encode(line[i:i+4]))
        print(encode(line))
        print(len(line))
        print(len(encode(line)))
    txt1.close()
    txt.close()
    txt1=open("out.txt",'r')
    txt2=open("out1.txt",'w')
    print("decode : " )
    for line in txt1:
        if (len(line)%3!=0):
            line+=(3-len(line)%3)*' '
        txt2.write(decode(line))
        print(decode(line))
        print(len(decode(line)))
    txt1.close()
    txt2.close()

main()        