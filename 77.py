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

def sum_possibilities(target,array): # Needs Nothing
	a=[1]+[0]*target
	for x in array:
		for i in range(x, target+1):
			a[i] += a[i-x]
	return a[target]

setprimes(100)

for i in range(10,100):
	if(sum_possibilities(i,prime)>=5000):
		print(i)
		input()