import math

def iridium(n): # Awesome Function
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

print(math.log10(3317044064679887385961981))
exit()

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def lienprime(n): # Needs iridium() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	I=iridium(n)
	for a in I:
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

def gcd(a,b):
	if a>b :
		x,y=a,b
	else:
		x,y=b,a

	if(x%y==0):
		return y
	return gcd(y,x%y)
	
def c(n):
	a=n-totient(n)
	b=n-1
	z=gcd(a,b)
	return [a//z,b//z]

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

prime=[]
dick={}
def setprimes(n): # Needs prime[]
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				dick[x]=False
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
			dick[x]=False

setprimes(100000)

s=0
for i in range(2,100000):
	cor=c(i)
	if cor[0]==1 and lienprime(i)==False:
		pf=primefac(i)[0]
		s+=i
		for y in pf:
			dick[y]=True
		print(i,cor,pf,s)

		# input()
print('\n\n\n')
for i in prime:
	print(i,end="  ")
	if dick[i]==False:
		print("FALSE",end="")
		input()
	else:
		print("       TRUE")
		