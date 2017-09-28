import math

def product(l):
	p=1
	for i in l:
		p*=i
	return p

def radical(n): # Needs math
	d=2
	i=-1
	factors=[]
	while(n>1):
		if(n%d==0):
			i+=1
			factors.append(d)
		while(n%d==0):
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
	return product(factors)

l=[]
for i in range(1,100001):
	r=radical(i)
	# print(i,r)
	l.append(r)

for i in range(0,len(l)):
	if(l[i]==1947):
		print(i)
