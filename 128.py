import math 

def f(x,k):
	if x==0:
		return 1
	if 3*x*x+k*x+2==int(3*x*x+k*x+2):
		return int(3*x*x+k*x+2)
	return 3*x*x+k*x+2

def x(n):
	if n==1:
		return 0
	return (3+math.sqrt(12*n-15))/6

def k(n):
	if(n==1):
		return 0
	y=int(x(n))
	return (n-2-3*y*y)/y

def neighbours(n):
	if n==1:
		return [2,3,4,5,6,7]

	if n==2:
		return [1,3,7,8,9,19]

	if n==7:
		return [1,2,6,17,18,19]
	h=int(x(n))
	if h==1:
		return sorted([n+1,n-1,f(h+1,k(n)),f(h-1,k(n)),f(h+1,k(n))+1,f(h+1,k(n))-1])

	if k(n)==-3:
		return sorted([f(h+1,-3),f(h+1,-3)+1,f(h+1,-3)-1,f(h+2,-3)-1,f(h-1,-3),n+1])

	if h!=int(x(n+1)):
		return sorted([n-1,f(h,-3),f(h,-3)-1,f(h-1,-3),f(h+2,-3)-1,f(h+2,-3)-2])

	if k(n)==int(k(n)):
		return sorted([n+1,n-1,f(h+1,k(n)),f(h-1,k(n)),f(h+1,k(n))+1,f(h+1,k(n))-1])

	return sorted([n+1,n-1,math.floor(f(h-1,k(n))),math.ceil(f(h-1,k(n))),math.floor(f(h+1,k(n))),math.ceil(f(h+1,k(n)))])

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

def pd(n):
	count=0
	for i in neighbours(n):
		if lienprime(math.fabs(i-n)):
			count+=1
	return count	

n=0
z=1
while True:
	i=f(z,-3)-1
	j=f(z,-3)
	if pd(i)==3:
		n+=1
		print(n,i)
		if n==2000:
			exit()
	if pd(j)==3:
		n+=1
		print(n,j)
		if n==2000:
			exit()
	z+=1