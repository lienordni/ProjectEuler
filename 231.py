import time

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

def exponent(n,p):
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def ncr_factors(n,r2):
	if(r2<n-r2):
		r=r2
	else:
		r=n-r2
	s=0
	for i in range(2,r+1):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(r,i)-exponent(n-r,i)				
			print(i,e)
			s+=i*e
	for i in range(r+1,n+1-r):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(n-r,i)
			print(i,e)
			s+=i*e
	for i in range(n+1-r,n+1):
		if(lienprime(i)):
			e=exponent(n,i)
			print(i,e)
			s+=i*e
	return s

start=time.clock()
print(ncr_factors(20000000,5000000))
end=time.clock()
print(end-start)