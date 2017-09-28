import math

def lienordni(n): # Awesome Lienordni Function (ALF)
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

def lienprime(n): # Needs lienordni() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	
	for a in lienordni(n):
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

prime=[]

def setprimes(n): # Needs prime[]
	life=open("./primes2.txt","r")
	x=0
	while True:
		x=int(life.readline())
		if x>n:
			return
		# print(x)
		prime.append(x)

setprimes(1000)

# print(prime)

def iscube(x):
	y=int(x**(1/3))
	# print(x,y)
	# input()
	return y**3==x or (y+1)**3==x

def ssup(p):
	for n in range(1,10000):
		if(iscube(n**3+n*n*p)):
			return n

	return 0;

# for p in prime:
# 	x=ssup(p)
# 	if(x==0):
# 		continue;

# 	print(p,x)



cubes=[]

for i in range(1,1000002):
	cubes.append(i**3)

niceprimes=[]

for i in range(1,1000001):
	q=cubes[i]-cubes[i-1]
	if(q>=1000000):
		print("broken")
		break
	if lienprime(q):
		niceprimes+=[q];

print(len(niceprimes))




