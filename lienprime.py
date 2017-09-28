import time
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

def arsenic(x,y,n): # Power Modulo
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=arsenic(x,y//2,n)
		return (z*z)%n
	return (x*arsenic(x,y-1,n))%n

def lienprime(n): # Needs iridium() and arsenic()
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
		x=arsenic(a,d,n)
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

def lithium(a,b): # 2x2 Matrix Multiplication 
	return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]]

def rhenium(x,y,n=None):	# 2x2 Modular Matrix Exponentiation, Needs Lithium()
	if n is None:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			return x
		if(y%2==0):
			z=rhenium(x,y//2)
			return lithium(z,z)

		return lithium(rhenium(x,y-1,n),x)


	else:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			z=[]
			for i in range(0,4):
				z.append(x[i]%n)
			return z
		if(y%2==0):
			z=rhenium(x,y//2,n)
			p=(lithium(z,z))
			q=[]
			for i in range(0,4):
				q.append(p[i]%n)
			return q

		f=lithium(rhenium(x,y-1,n),x)
		g=[]
		for i in range(0,4):
			g.append(f[i]%n)
		return g

'''
print(rhenium([1,1,1,0],8))
exit(0)
'''

def fibonacci(n,m=None): #Needs lithium(), rhenium()
	a=[1,1,1,0]

	if m is None:
		b=rhenium(a,n)
	else:
		b=rhenium(a,n,m)

	return b[1]

start=time.clock()
print(fibonacci(10**200,10000000007))
end=time.clock()
print(end-start)
exit(0)

def isprime(x): # Needs math
	if(x<2):
		return False
	if(x==2 or x==3 or x==5 or x==7):
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if(x%i==0):
			return False
	return True

count=0


lower=10**14
num=10**5
mod=1234567891011


i=lower
sum=0
start=time.clock()
while(count<num):
	if(lienprime(i)):
		count+=1;
		# if(count%100==0):
		# 	print(count)
		qwe=fibonacci(i,mod)
		# print(count,i,qwe)
		sum+=fibonacci(i,mod)
		sum%=mod
		
	i+=1

end=time.clock()
print(sum)
print(end-start)
