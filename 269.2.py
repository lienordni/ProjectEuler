import math

def primefac(n): # Needs math
	d=2
	i=-1
	factors=[]
	indices=[]
	while(n>1):
		if(n%d==0):
			i+=1
			factors.append(d)
			indices.append(0)
		while(n%d==0):
			indices[i]+=1
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def lienordni(n,k):
	l=lien(n)
	l.reverse()
	s=0
	for i in range(0,len(l)):
		s+=l[i]*(k**i)
	return s==0

q=-2
for i in range(9,1500):
	if lienordni(i,q):
		l=lien(i)
		l.reverse()
		for k in range(0,len(l)):
			l[k]=l[k]*(10**k)/(10-q)
		l.reverse()
		print(i,l,sum(l))
