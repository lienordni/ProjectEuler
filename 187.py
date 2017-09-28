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

def lienposition(x,l): # Needs nothing
	if(len(l)==0):
		return 0
	if(l[-1]<x):
		return len(l)
	if(len(l)==1 and l[0]==x):
		return 0
	low=0
	high=len(l)-1
	if(x==l[low]):
		return low+1
	if x==l[high]:
		return high+1
	if(x<l[low] or x>l[high]):
		return 0
	while True:
		mid=(low+high)//2
		if(mid==low):
			return mid+1

		if(x>l[mid]):
			low=mid
			continue
		elif(x<l[mid]):
			high=mid
			continue
		else:
			return mid+1
	
def primepi(n): # Needs setprimes(), prime[], lienposition()
	if n>prime[-1]:
		return len(prime)
	if n<=0:
		return 0
	x=lienposition(n,prime)
	return x

n=10**8
setprimes(n//2)
s=0
i=0
while prime[i]**2<=n:
	q=primepi(n//prime[i])-primepi(prime[i]-1)
	print(prime[i],q)
	s+=q
	i+=1
print(s)
# print(prime)

