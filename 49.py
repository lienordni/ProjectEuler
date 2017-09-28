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

setprimes(10000)
prime=prime[168:]

def contain(x,l):
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

def ispr(x):
	if(x<=1):
		return False
	return (contain(x,prime))

def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def vodka(x,y,z):
	a=sorted(lien(x))
	b=sorted(lien(y))
	c=sorted(lien(z))
	return (a==b and b==c)

for i in range(1,1061):
	for j in range(0,i):
		if contain(2*prime[i]-prime[j],prime[(i+1):]) and vodka(prime[j],prime[i],2*prime[i]-prime[j]):
			print(prime[j],prime[i],2*prime[i]-prime[j])
