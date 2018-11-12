# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:25:56 2018

@author: reddy
"""
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    if n==1 :
        return False
    return True
def main():
    inputlist=[]
    print (" number of number to be entered ")
    num=int(input())
    print (" enter the numbers ")
    for i in range(num):
        temp=int(input())
        inputlist.append(temp)
    result = False
    primelist=[]
    for i in inputlist :
        if(isPrime(i)) :
            primelist.append(i)
    print ("  enter sum ")
    sum1=int(input())
    for i in range((2**len(primelist))):#to generate all possibe combinations 
        c=0
        sum2=0
        i2=i
        while i2>0 : # to check if we are considering the digit
            sum2=sum2+(i2%2)*primelist[c]
            c+=1
            i2=i2>>1
        if sum2==sum1:
            result = True 
            break 
    if result:
        print ("ok")
        print ("combination :")
        c=0
        while i>0 :
            if (i%2) :
                print(primelist[c])
            c+=1
            i=i>>1
    else :
        print ("false")
main()
    