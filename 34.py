import math

def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def su(x):
	s=0
	for i in range(0,len(lien(x))):
		s+=math.factorial(lien(x)[i])
	return s

def AWUS036H(x):
	return x==su(x)


i=10
s=0
while True:
	if AWUS036H(i):
		s+=i
		print(i,s)
	i+=1