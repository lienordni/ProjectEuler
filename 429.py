import math

prime=[]

def setprimes(n): # Needs prime[]
	life=open("./primes2.txt","r")
	x=0
	while True:
		x=int(life.readline())
		if x>n:
			return
		# print(x)
		prime.append(x)

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

def factors2(n): # O(n^(1/2))
	l=[]
	for i in range(1,1+int(math.sqrt(n))):
		if n%i==0:
			if i*i!=n:
				l+=[i,n//i]
			else:
				l+=[i]

	l.sort()
	return l

def gcd(a,b):
	r=b
	s=a
	while r!=0:
		q= s//r
		t=r
		r=s-q*t
		s=t
	return s

def sos(l):
	s=0
	for i in l:
		s+=i*i
	return s

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

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def cleanse(l): # Gets rid of Redundancies in a sorted array
	m=[l[0]]
	for i in range(1,len(l)):
		if l[i]!=l[i-1]:
			m+=[l[i]]
	return m

setprimes(1000000)

def factorial_factorization(n): # Needs setprimes()
	bases=[]
	exponents=[]
	for	p in prime:
		bases.append(p)
		exponents.append(exponent(n,p))
	return [bases,exponents]

def factorial_factors(n): # Needs primefac(), inc(x,y), power(), math, factorial_factorization(), exponent(), setprimes(), prime[]
	f=factorial_factorization(n)
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
	ans=cleanse(ans)
	return ans

for i in range(2,6):
	print(i,factorial_factors(i),factorial_factorization(i))

exit()
def unitary(n):
	l=[]
	f=math.factorial(n)
	# print(factorial_factors(n))
	# print(f)
	for i in factorial_factors(n):
		# print("F",i)
		if gcd(i,f//i)==1:
			l.append(i)
	return l


i=2
array=[0]*21
while i<=30:
	u=unitary(i)
	sus=sos(u)	
	print(i,sus)
	input()
	i+=1

print(array)
exit()
array=[0, 0, 5, 50, 650, 16900, 547924, 27396200, 1746641000, 139773881000, 13460683752200, 1642203417768400, 236441876606410000, 40195119023089700000, 7723888546922636420000, 1735183690969722609168800, 444206919394766468845892000, 128820006624482275965308680000, 41737604550102658693597600532800]

for i in range(4,19):
	print(i,array[i]%5)

