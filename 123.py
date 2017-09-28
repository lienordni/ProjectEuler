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

setprimes(1000000)

def p(n):
	return prime[n-1]

def r(n):
	return (((p(n)-1)**n)+((p(n)+1))**n)%(p(n)**2)

def r2(n):
	if n%2==0:
		return 2
	return 2*n*p(n)

i=1
while True:
	a=r2(i)
	print(i,a)
	if a>=10**10:
		input()
	i+=2



