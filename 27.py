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

def contain(x,l):
	low=0
	high=len(l)-1
	if(x==l[low] or x==l[high]):
		return True
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

setprimes(100000)
'''
for i in range(1,98):
	if(ispr(i)):
		print(i)
#print(prime)
'''
best=0
for b in prime[12:]:
	for a in range(-b-1,1001):
		n=0
		while ispr(n*n+a*n+b):
			n+=1
		if(n>best):
			best=n
			print("n^2 +",a,"*n +",b,"---> ",n)
		