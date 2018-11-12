# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:23:26 2018

@author: reddy
"""

#Question 3         using List
d=dict()
name=""
mat=[]
soc=[]
sci=[]
num=int(input("Enter number of students"))
fil=open("New.txt",'w')
for i in range(num):
    name=(input("Enter names"))
    d[name]=[]
    d[name].append(int(input("Enter maths marks "")))
    d[name].append(int(input("Enter science marks")))
    d[name].append(int(input("Enter social marks")))
    
	
	
	
	
print(d)
minn=301
low_name=""
high_mat=-1
high_name_m=""
low_mat=101
high_soc=-1
high_name_soc=""
low_soc=101
low_name_soc=""
high_sci=-1
high_name_sci=""
low_sci=101
low_name_sci=""
maxx=-1
high_name=""
low_name_m=""
for key, value in d.items():
    if minn>(value[0]+value[1]+value[2]):
        minn=value[0]+value[1]+value[2]
        low_name=key
    if maxx<(value[0]+value[1]+value[2]):
        maxx=value[0]+value[1]+value[2]
        high_name=key
    if(low_mat>value[0]):
        low_mat=value[0]
        low_name_m=key
    if(high_mat<value[0]):
        high_mat=value[0]
        high_name_m=key
    if(low_sci>value[1]):
        low_sci=value[1]
        low_name_sci=key
    if(high_sci<value[1]):
        high_sci=value[1]
        high_name_sci=key
    if(low_soc>value[2]):
        low_soc=value[2]
        low_name_soc=key
    if(high_soc<value[2]):
        high_soc=value[2]
        high_name_soc=key
    

high_tot=maxx
low_tot=minn
maxx=0
minn=100

fil.write("Highest maths:%d Marks\n"%high_mat)
fil.write("highest maths by: "+high_name_m)
fil.write("\nlowest maths :%d Marks\n"%low_mat)
fil.write("low maths marks by:"+low_name_m)

fil.write("\nHighest science:%d Marks\n"%high_sci)
fil.write("highest science by:"+high_name_sci)
fil.write("\nlowest science :%d Marks\n"%low_sci)
fil.write("low science marks by:"+low_name_sci)

fil.write("\nHighest social:%d Marks\n"%high_soc)
fil.write("highest social marks by:"+high_name_soc)
fil.write("\nlowest social :%d Marks\n"%low_soc,)
fil.write("low social marks by:"+low_name_soc)

fil.write("\nHighest total:%d Marks\n"%high_tot)
fil.write("highest total by:"+high_name)
fil.write("\nlowest total :%d Marks\n"%low_tot)
fil.write("lowest total by:"+low_name)
fil.close()
