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

setprimes(100)
c=6
for i in prime[2:]:
	x=c
	for k in range(1,i):
		print(x)
		x+=c
		if(x>10**6):
			input()
	c*=i

print(p)
