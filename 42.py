import math

def tri(x):
	return (-1+math.sqrt(1+8*x))/2==int((-1+math.sqrt(1+8*x))/2)

xin=open("42.txt","r")
py=(xin.read()).split("\",\"")

def value(string):
	s=0
	for i in range(0,len(string)):
		s+=(ord(string[i])-64)
	return s

count=0
for dk in py:
	if(tri(value(dk))):
		count+=1

print(count)