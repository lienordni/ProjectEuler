def lienordni(n): # Awesome Lienordni Function
	if(n<2047):
		return [2]
	if(n<1373653):
		return [2,3]
	if(n<9080191):
		return [31,73]
	if(n<25326001):
		return [2,3,5]
	if(n<4759123141):
		return [2,7,61]
	if(n<1122004669633):
		return [2,13,23,1662803]
	if(n<2152302898747):
		return [2,3,5,7,11]
	if(n<3474749660383):
		return [2,3,5,7,11,13]
	if(n<341550071728321):
		return [2,3,5,7,11,13,17]
	if(n<3825123056546413051):
		return [2,3,5,7,11,13,17,19,23]
	if(n<318665857834031151167461):
		return [2,3,5,7,11,13,17,19,23,29,31,37]
	if(n<3317044064679887385961981):
		return [2,3,5,7,11,13,17,19,23,29,31,37,41]

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def lienprime(n): # Needs lienordni() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	
	for a in lienordni(n):
		x=power_modulo(a,d,n)
		if(x==1):
			continue
		over=False
		for r in range(0,s):
			if(x==n-1):
				over=True
				break
			x=(x*x)%n

		if(over):
			continue

		return False

	return True

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def ncr_factors(n,r2): # Prime factorization of binomial_coefficients(n,r) # Needs lienprime() and exponent()
	if(r2<n-r2):
		r=r2
	else:
		r=n-r2
	s=0
	a=[]
	b=[]
	for i in range(2,r+1):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(r,i)-exponent(n-r,i)				
			if(e>0):
				a+=[i]
				b+=[e]
	for i in range(r+1,n+1-r):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(n-r,i)
			if(e>0):
				a+=[i]
				b+=[e]
	for i in range(n+1-r,n+1):
		if(lienprime(i)):
			e=exponent(n,i)
			if(e>0):
				a+=[i]
				b+=[e]
	return [a,b]

def contain(x,l): # Needs nothing
	if(len(l)==0):
		return False
	if(len(l)==1):
		return x==l[0]
	low=0
	high=len(l)-1
	if(x==l[low] or x==l[high]):
		return True
	if(x<l[low] or x>l[high]):
		return False
	while True:
		mid=(low+high)//2
		if(mid==low):
			return False

		if(x>l[mid]):
			low=mid
			continue
		elif(x<l[mid]):
			high=mid
			continue
		else:
			return True

def squarefree(n,r,l):
	f=l[1]
	return max(f)<=1

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

def cleanse(l): # Gets rid of Redundancies in a sorted array
	m=[l[0]]
	for i in range(1,len(l)):
		if l[i]!=l[i-1]:
			m+=[l[i]]
	return m

l=[1]
for n in range(2,51):
	for r in range(1,1+n//2):
		b=ncr_factors(n,r)
		if squarefree(n,r,b):
			l.append(power(b[0],b[1]))

l.sort()
l=cleanse(l)
print(l,sum(l))


