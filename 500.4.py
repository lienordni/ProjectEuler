import sys
import math
sys.setrecursionlimit(500501)

def power(l,mod=None): # = product(a[i]**b[i]) # Needs Nothing
	s=1
	if mod!=None:
		for i in range(0,len(l[0])):
			s=(s*(l[0][i]**l[1][i]))%mod
	else:
		for i in range(0,len(l[0])):
			s=s*(l[0][i]**l[1][i])
	return s


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

def next_prime(n):
	c=n+2
	if n%2==0:
		c-=1
	while True:
		if lienprime(c):
			return c
		c+=2


prime=[2,3]

def nextprime(n=None): # Needs prime[]
	if n==None:
		x=prime[-1]+2
	else:
		x=n+2
	while True:
		if(x==5 or x==7):
			prime.append(x)
			return x

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if c:
			prime.append(x)
			return x
		x+=2

'''
print(nextprime(3))
print(nextprime(5))
print(nextprime(5))
print(nextprime(7))
print(nextprime(7))
print(nextprime(7))
print(nextprime(11))
print(nextprime(13))
print(nextprime(17))
print(nextprime(17))
exit()
'''

function=[0,[[2],[1]],[[2,3],[1,1]]]
# exit()
def function(x):
	if x==1:
		return [[2],[1]]
	if x==2:
		return [[2,3],[1,1]]
	y=list(function(x-1))
	np=nextprime(y[0][-1])
	for i in range(len(y[0])):
		if (y[1][i]+1)<math.log(np,y[0][i]):
			y[1][i]+=(y[1][i]+1)
			# print(x)
			return y
			continue
	y[0].append(np)
	y[1].append(1)
	# print(x)
	return y

print(power(function(26181),500500507))
