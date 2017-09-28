prime=[]

def setprimes(n):
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

def isprime(x):
	if(x<2):
		return False
	if(x==2 or x==3 or x==5 or x==7):
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if(x%i==0):
			return False
	return True


def lienordni(x):
	l=lien(x)
	for i in range(1,len(l)):
		if(isprime(antilien(l[i:]))==False or isprime(antilien(l[:i]))==False):
			return False
	return True
'''

def lienordni(x):
	l=lien(x)
	for i in range(1,len(l)):
		print(antilien(l[i:]))
		print(antilien(l[:i]))
'''
'''
print(isprime(2))
print(isprime(9))
print(lienordni(29))
exit(0)
'''
print("Setting Primes..")
setprimes(10**6)
print("Primes Set...")
s=0
for p in prime[4:]:
	if(lienordni(p)):
		print(p)
		s+=p
print()
print("sum = ",s)