import math

def primefac(n): # Needs nothing
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
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def issquare(n):
	if(n<2):
		return True
	return (int(math.sqrt(n))*int(math.sqrt(n))==n)

def sos(n):
	i=1
	a=[]
	while i<=int(math.sqrt(n/2)):
		if issquare(n-i*i):
			a.append([i,int(math.sqrt(n-i*i))])
		i+=1
	if(len(a)>0):
		return a
	return 0

def rat(p):
	count=0
	for c in range(5,int(p/math.sqrt(2))+1):
		e=sos(c**2)
		if(e!=0):
			for i in e:
				a=i[0]
				b=i[1]
				if(a+b+c!=p):
					continue
				# print(a,',',b,',',c)
				count+=1
	return count

for p in range(12,1000):
	if(rat(p)==1):
		print(p)