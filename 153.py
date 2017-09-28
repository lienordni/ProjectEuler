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

def inc(x,y): # Increments a number array x with variable base array y # Needs nothing
	l=len(y)
	if(x[l-1]!=y[l-1]-1):
		x[l-1]+=1
		return x

	p=l-1
	while p>=0:
		if(x[p]!=y[p]-1):
			x[p]+=1
			for k in range(p+1,l):
				x[k]=0
			return x
		p-=1
	for i in range(0,l):
		x[i]=0
	return x

def power(a,b,m=None): # = product(a[i]**b[i]) # Needs Nothing
	if m==None:
		s=1
		for i in range(0,len(a)):
			s*=a[i]**b[i]
		return s

	s=1
	for i in range(0,len(a)):
		s*=(a[i]%m)**b[i]
		s%=m
	return s

def factors(n): # Needs primefac(), inc(), power(), math
	f=primefac(n)
	p=f[0]
	i=f[1]
	y=[]
	number=1
	for k in range(0,len(i)):
		y.append(i[k]+1)
		number*=i[k]+1
	x=[0]*len(p)
	ans=[]
	for k in range(0,number):
		ans.append(power(p,x))
		inc(x,y)
	ans.sort()
	ans.pop()
	return ans

def gaussianfactors(n):
	s=0
	l=[]
	for a in range(1,n+1):
		for b in range(0,int(math.sqrt(n*a-a*a))+1):
			if (n*a)%(a*a+b*b)==0 and (n*b)%(a*a+b*b)==0:
				if b==0:
					# if a!=n:
					# 	print(a,end=", ")
					# else:
					# 	print(a,end="")
					l.append([a,0])
				else:
					# print(a,end="+i")
					# if b!=1:
					# 	print(b,end="")
					# print(end=", ")
					# print(a,end="-i")
					# if b!=1:
					# 	print(b,end="")
					# print(end=", ")
					l.append([a,b])
					l.append([a,-b])
	return l

def sogf(n):
	f=gaussianfactors(n)
	s=0
	for i in f:
		s+=i[0]
	return s

def gcd(a,b): # Copied From Wikipedia, No fucking idea how it works.
	r=b
	old_r=a
	while r!=0:
		quotient=old_r//r

		prov=r
		r=old_r-quotient*prov
		old_r=prov

	return old_r

def allreal(g):
	for i in g:
		if i[1]!=0:
			return False
	return True

def listsub(a,b):
	c=[]
	for i in a:
		if i not in b and gcd(i[0],i[1])==1:
			c.append(i)
	return c


def new(n):
	l=gaussianfactors(n)
	for i in factors(n):
		l=listsub(l,gaussianfactors(i))
	return l

def sos(a):
	return a[0]**2+a[1]**2

def primitive(g):
	l=[]
	for i in g:
		if gcd(i[0],i[1])==1:
			l.append(i)

	return l;

s=1
limit=10
m=0

for n in range(2,limit+1):
	q=sogf(n)
	s+=q
	g=gaussianfactors(n)
	# l=primitive(g)
	print(n,g,q)
	# if([1,3] in g or [1,-3] in g or [3,1] in g or [3,-1] in g):
	# if([3,9] in g):
	# 	print(n,g)	
	# for i in l:
	# 	if sos(i)>m:
	# 		m=sos(i)
	
	# s+=q
#	g=gaussianfactors(n)
#	if allreal(g):
#		print(n,g)
#		print("\n","-"*30)
#	for c in g[:(-1)]:
#		# print(c[0]**2+c[1]**2)
#		if(c[0]**2+c[1]**2>m):
#			m=c[0]**2+c[1]**2
#	s+=q
	# print()
	# print("ALL : ",gaussianfactors(n))
	# q=new(n)
	# print("NEW : ",q)
	# if(len(q)!=0):
	# 	input()
	# print()
print(s,m)
