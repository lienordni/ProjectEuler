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

print("Setting Primes..")
setprimes(10**6)
print("Primes Set..")
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

#print(antilien([4,3,2,7]))

def rotate(l):
	if(len(l)==1):
		return l
	return l[1:]+[l[0]]
	

#print(rotate(18236))

def isprime(x):
	return x in prime
'''
print(isprime(32))
exit(0)
'''
count=0
for p in prime:
	circ=True
	x=p
	l=lien(x)
	for i in range(0,len(l)-1):
		l=rotate(l)
		y=antilien(l)
		if(isprime(y)==False):
			circ=False
			break
#	x=rotate(x)
	if(circ):
		print(p)
		count+=1
#		input()

print(count)

#ANSWER : 55