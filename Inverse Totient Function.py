import sys
import math
import time

def primefac(n): # Needs math
	d=2
	i=-1
	bases=[]
	indices=[]
	while(n>1):
		if(n%d==0):
			i+=1
			bases.append(d)
			indices.append(0)
		while(n%d==0):
			indices[i]+=1
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		bases.append(n)
		indices.append(1)
	return [bases,indices]

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

def factors(n): # Needs primefac(), inc(x,y), power(), math
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
	return ans

def factorial_factors(n): # Needs primefac(), inc(x,y), power(), math
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
	return ans

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

prime=[]

def setprimes(n): # Needs prime[]
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				continue
			else:
				continue

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if(c):
			prime.append(x)

def factorial_factorization(n): # Needs setprimes()
	setprimes(n)
	bases=[]
	exponents=[]
	for	p in prime:
		bases.append(p)
		exponents.append(exponent(n,p))
	return [bases,exponents]

def lienordni(n): # Awesome Lienordni Function (ALF)
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

def totient(n): # Needs lienprime() and primefac()
	if(n==1):
		return 1
	if(lienprime(n)):
		return (n-1)
	x=primefac(n)[0]
	m=n
	for i in x:
		m-=m//i
	return m


IV=[[]]*10000000

def factors2(n):
	l=[]
	for i in range(1,1+int(math.sqrt(n))):
		if n%i==0:
			if i*i!=n:
				l+=[i,n//i]
			else:
				l+=[i]

	l.sort()
	return l

def inverse_totient(m): # Needs IV[[]], factors(), primefac(), inc(x,y), power(), math
	print("***************",m,"*"*10)	
	# if m<10000000:
	# 	if len(IV[m])!=0:
	# 		return IV[m]
	if m==1:
		return [1,2]

	facs=factors2(m)
	primelist=[]
	for i in facs:
		if lienprime(i+1):
			primelist.append(i+1)
	primelist.reverse()
	print("primelist = ",primelist)
	# return
	final=[]
	for p in primelist[:(-1)]:
		k=0
		c=m
		while(c%p==0):
			c//=p
			k+=1

		result=[]
		for d in range(1,k+2):
			x=m//((p-1)*(p**(d-1)))
			if x%2==1 and x>1:
				continue
			print("X = ",x)
			temp=inverse_totient(x)
			print("temp =",temp)
			l=[]
			for j in temp:
				if j==1:
					final.append(p**d)
					print(m,"appended : ",p**d)
					print(final)
				elif primefac(j)[0][0]>p:
					final.append(j*(p**d))
					print(m,"appended : ",j*(p**d))
					print(final)
			print(m,"Vector :",final)

	final+=[2*i for i in final]

	p=2
	k=0
	c=m
	while(c%p==0):
		c//=p
		k+=1

	for d in range(2,k+2):
		x=m//(2**(d-1))
		if x%2==1 and x>1:
			continue
		temp=inverse_totient(x)
		l=[]
		for j in temp:
			if j==1:
				final.append(2**d)
			elif primefac(j)[0][0]>p:
				final.append(j*(2**d))

	# final.sort()
	return final

# def inverse_totient(m,that=None):
# 	print("---",m,"---")
# 	facs=factors(m)
# 	primelist=[]
# 	for i in facs:
# 		if lienprime(i+1):
# 			primelist.append(i+1)

# 	# print(primelist)
# 	final=[]
# 	for p in primelist:
# 		k=0
# 		c=m
# 		while(c%p==0):
# 			c//=p
# 			k+=1
# 		for d in range(1,k+2):
# 			print(p,d)
# 			if(p==2 and d==1):
# 				continue;


# print(len(sys.argv))

# for i in range(1,10001):
# 	print(i,inverse_totient(i))
# exit()

# x=math.factorial(13)
# inverse_totient(x)
# exit()


n=int(sys.argv[1])
start=time.time()
inv=inverse_totient(n)
end=time.time()
print(inv)
print("Time Taken : ",end-start)

