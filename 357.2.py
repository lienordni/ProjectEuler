import math

def contain(x,l): # Needs nothing
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

def allprime(n):
	if n in [1,2,6]:
		return True
	for i in range(1,1+int(math.sqrt(n))):
		if n%i!=0:
			continue
		if contain(i+n//i,prime)==False:
			return False
	return True

prime=[]

def genprimes(n): # Needs prime[]
	s=0
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				if x%4 in [2,3]:
					print(x,end="  ")
					if(allprime(x-1)):
						print("YO",x-1)
						s+=x-1
					else:
						print()
					# input()
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
			if x%4==3:
				print(x,end="  ")
				if(allprime(x-1)):
					print("YO",x-1)
					s+=x-1
				else:
					print()
				# input()
	return s

print(genprimes(10**8))
