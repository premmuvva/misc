# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 00:00:47 2018

@author: reddy
"""

# -*- coding: utf-8 -*-

def main():
    s=input()
    length=len(s)
    s=s+'$'
    count=1
    for i in range (length):
        if(s[i]== s[i+1]):
            count+=1
        else:
            if ((s[i+1]>='0'and s[i+1]<='9')or(s[i]>='0'and s[i]<='9')) :
                if (count == 1):
                    print(s[i],end=".")
                elif ((s[i]>='0'and s[i]<='9')):
                    print(s[i],'x',count,sep="",end=".")
                else:
                    print(s[i],count,sep="",end=".")
            else:
                if (count == 1):
                    print(s[i],end="")
                else:
                    print(s[i],count,sep="",end="")
            count = 1
main()