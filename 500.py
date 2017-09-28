prime=[]

def setprimes(n): # Needs prime[]
	product=1
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				product*=x
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
			product*=x
			product%=500500507
			prime.append(x)
	return product

print(setprimes(7376507))

