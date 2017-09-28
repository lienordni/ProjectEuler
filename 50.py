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

lim=int(input())
print("Setting Primes...")
setprimes(lim)
print("Primes Set.")

i=0

truemaxvalue=0
truemaxlength=0
while i<len(prime)-1:
	s=prime[i]
	l=0
	j=i+1
	maxsum=prime[i]
	maxlength=1
	while s<lim and j<len(prime):
		s+=prime[j]
		if(ispr(s)):
			maxsum=s
			maxlength=j+1-i
		j+=1

	# if(maxlength==543):
	# 	for k in range(0,maxlength):
	# 		print(prime[i+k],end=" ")
	# 	print()
	# 	print("Length = ",maxlength,"\nSum = ",maxsum)
	# 	input()
	if(maxlength>truemaxlength):
		truemaxlength=maxlength
		truemaxvalue=maxsum

	i+=1

# print()
print("True max value : ",truemaxvalue)
print("True max length : ",truemaxlength)