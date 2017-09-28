import math

def binary(i,size=None):
	s=bin(i)
	lol=[int(x) for x in s[2:]]
	if(size!=None):
		lol=[0]*(size-len(lol))+lol
	return lol

def isprime(x): # Needs math
	if(x<2):
		return False
	if(x==2 or x==3 or x==5 or x==7):
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if(x%i==0):
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
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

num=int(input())

def phi(z):
	return (3+z)//2;

print(primefac(num))
input()

def gcd(a,b):
	if a>b :
		x,y=a,b
	else:
		x,y=b,a

	if(x%y==0):
		return y
	return gcd(y,x%y)
	
def psi(p):
	c=0
	i=2-p%2
	q=0
	a=[]
	b=[]
	while i<= ((p+2*(p%3))/3)-2 :
		if gcd(i,(p-i*3)//2)==1 :
			# print(i,(p-i*3)//2)
			# print(i,end="  ")
			# if(isprime(i)):
			# 	print("PRIME")
			# else:
			# 	print()
			a.append(i)
			# if(isprime(i)):
			# 	b.append(i)
			# # input()
			# q=i
			# input()
			# if(i%4!=0):
			# 	input()
		else:
			b.append(i)
		i+=2
	return [a,b]

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

def count(x,i):
	c=0
	t=i
	while t%x==0:
		c+=1
		t/=x
	return c

h=psi(num)
a=h[0]
b=h[1]

print()

i=1
c=0
d=0
while i<num/3:
	if contain(i,b) :
		d+=1
		print(i,",",(num-3*i)//2,"  ",end="  ")
		if(isprime(i)):
			print("PRIME"," "*50,"<",d,">")
		else:
			p=1
			for x in primefac(num)[0]:
				if(i%x==0):
					co=count(x,i)
					print(x,"^",co,end="  ")
					p*=x**co
			qwe=contain(i//p,a)
			print('=',i//p,qwe," "*50,"<",d,">")
			if(qwe==False):
				input()
	else:
		c+=1
		print(i,",",(num-3*i)//2,"  "," "*40,"(",c,")")

	i+=2

print("Answer :",len(a),"* 2 =",2*len(a))
# 6008819575

'''
i=11
while True:
	x=psi(phi(i))
	if(x>1):
		print(i,x)
		input()
	i+=1

print(2*psi(phi(13)))
'''