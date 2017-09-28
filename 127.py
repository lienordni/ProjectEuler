def gcd(a,b): # Copied From Wikipedia, No fucking idea how it works.
	r=b
	old_r=a
	while r!=0:
		quotient= old_r//r

		prov=r
		r=old_r-quotient*prov
		old_r=prov

	return old_r

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
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def rad(n):
	x=primefac(n)[0]
	p=1
	for i in x:
		p*=i
	return p

def abc(a,b,c):
	if a>=b:
		return False
	if gcd(a,b)!=1:
		return False
	if gcd(a,c)!=1:
		return False
	if gcd(c,b)!=1:
		return False
	if rad(a*b*c)>=c:
		return False
	return True

c=3
count=0
s=0
while True:
	tc=0
	for a in range(1,1+c//2):
		b=c-a
		if abc(a,b,c):
			print(a,b,c,end="  \n")
			# print(primefac(c))
			count+=1
			tc+=1
			s+=c
			# input()
	# print('\n\n',c,tc)
	# input()
	c+=1
	if c>1000:
		break

print(count,s)