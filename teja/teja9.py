# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:37:48 2018

@author: reddy
"""

task={}
max=0
with open("1.txt") as txt:
	lines=txt.readlines()
	tasks=int(lines[0])
	int(lines[1])
	for i in range(0,tasks):
		task[i]=int(lines[i+1])
		if (task[i]>max):
		   max = task[i]
print(tasks)
print(task)
depend=int(lines[tasks+1])
print(depend)
dep=[]
for i in range (tasks+2,len(lines)):
    dep.append(lines[i].split())
    #dep[-1].append(0)
    dep[-1]=[int(dep[-1][0]),int(dep[-1][1])]
fdep=[]
for i in range(len(dep)):
    check = 0
    for j in range(i,len(dep)):
        if (dep[i][1]==dep[j][0]):
            check=1
            fdep=fdep+[dep[i]]
            break
    if check == 0:
        fdep=[dep[i]]+fdep
print(fdep)
for i in range(len(fdep)-1,-1,-1):
    task[fdep[i][0]]+=task[fdep[i][1]]
    if (max<task[fdep[i][0]]):
        max=task[fdep[i][0]]
print(max)

"""def pattern(depend):
	print("Enter the task combinations with spaces")
	for i in range(depend):
		s=lines[tasks+2+i]
		dep.append(s.split())
	print(dep)

pattern(depend)
tot=[]
for i in range(len(dep)):
	tot.append(int(dep[i][0]))
	tot.append(int(dep[i][1]))
print(tot)

extra_time=0
for i in range(tasks):
	if i not in tot:
		extra_time+=task[i]
tot1=list(set(tot))
time=0
t1=0
for i in tot1:
	time=task[i]+time
if(int(dep[0][0]) not in dep[1]):
	if(int(dep[0][1]) not in dep[1]):
		if((task[int(dep[0][0])]+task[int(dep[0][1])])>(task[int(dep[1][0])]+task[int(dep[1][1])])):
			t1=task[int(dep[0][0])]+task[int(dep[0][1])]
			
		else:
			t1=(task[int(dep[1][0])]+task[int(dep[1][1])])
			
if t1==0:
	if time>=extra_time:
		print("Shortest time in minutes is: ",time)
	else:
		print("Shortest time in minutes is: ",extra_time)
else:
	if t1>=extra_time:
		print("Shortest time in minutes is: ",t1)
	else:
		print("Shortest time in minutes is: ",extra_time)
"""
