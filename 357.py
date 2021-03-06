import math

def iridium(n): # Awesome Function
	if(n<2047):
		return [2]
	if(n<1373653):
		return [2,3]
	if(n<9080191):
		return [31,73]
	if(n<25326001):
		return [2,3,5]
	if(n<4759123141):
		return [2,7,61]
	if(n<1122004669633):
		return [2,13,23,1662803]
	if(n<2152302898747):
		return [2,3,5,7,11]
	if(n<3474749660383):
		return [2,3,5,7,11,13]
	if(n<341550071728321):
		return [2,3,5,7,11,13,17]
	if(n<3825123056546413051):
		return [2,3,5,7,11,13,17,19,23]
	if(n<318665857834031151167461):
		return [2,3,5,7,11,13,17,19,23,29,31,37]
	if(n<3317044064679887385961981):
		return [2,3,5,7,11,13,17,19,23,29,31,37,41]

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def lienprime(n): # Needs iridium() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	
	for a in iridium(n):
		x=power_modulo(a,d,n)
		if(x==1):
			continue
		over=False
		for r in range(0,s):
			if(x==n-1):
				over=True
				break
			x=(x*x)%n

		if(over):
			continue

		return False

	return True

def primefac(n): # Needs nothing
	d=2
	i=-1
	factors=[]
	indices=[]
	while(n>1):
		if(n%d==0):
			i+=1
			factors.append(d)
			indices.append(0)
		while(n%d==0):
			indices[i]+=1
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def inc(x,y): # Increments a number array x with variable base array x # Needs nothing
	l=len(y)
	if(x[l-1]!=y[l-1]):
		x[l-1]+=1
		return x

	p=l-1
	while p>=0:
		if(x[p]!=y[p]):
			x[p]+=1
			for k in range(p+1,l):
				x[k]=0
			return x
		p-=1
	for i in range(0,l):
		x[i]=0
	return x

def power(a,b): # = product(a[i]**b[i]) # Needs Nothing
	s=1
	for i in range(0,len(a)):
		s*=a[i]**b[i]
	return s

def allprime(n):
	p=primefac(n)
	l=len(p[1])
	num=1
	for x in p[1]:
		num*=x+1
	x=[0]*l
	for i in range(0,num):
		z=(power(p[0],x))
		if lienprime(z+n//z)==False:
			return False
		inc(x,p[1])
	return True

# def allprime(n):
# 	f=factors(n)
# 	for x in f[:((len(f)+1)//2)]:
# 		if lienprime(x+(n//x))==False:
# 			return False
# 	return True

x=10
i=4
s=9
while x<=100000000:
	if allprime(x):
		print(i,x,primefac(x))
		input()
		s+=x
		i+=1
	x+=4
	# if(x%10 in [4,6]):
	# 	x+=(8-x%10)
print(s)