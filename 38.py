import math

def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li):
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def pro(x,l):
	r=[]
	for i in l:
		r+=lien(x*i)
	return r

def pand(l,size):
	x=sorted(l)
	# print(x)
	# print(list(range(1,10)))
	return (x==list(range(1,size+1)))

for size in range(2,10):
	x=[i for i in range(1,size+1)]
	n=1
	p=1
	while p<10**10:
		p=antilien(pro(n,x))
		if(pand(lien(p),9)):
			print(n,"*",x,"=",p)
		n+=1
