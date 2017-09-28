import math
import time



'''
start=time.clock()
n=5145940800
for i in range(2,n//2+1):
	if(n%i==0):
		print(i)
end=time.clock()
print(end-start)
exit(0)
'''
def primefac(n):
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

def inc(x,y):
	if(x[0]!=y[0]):
		x[0]+=1
		return x

	for p in range(1,len(y)):
		if(x[p]!=y[p]):
			x[p]+=1
			x[:p]=[0]*p
			return x
	return [0]*len(y)

#21621600
'''
n=5145940800
l=primefac(n)
a=l[0]
y=l[1]
x=[0,0,0,0,0,0,0]
start=time.clock()
for i in range(0,2016):
	s=1
#	print(a)
#	print(x)
	for n in range(0,len(a)):
		s*=a[n]**x[n]
	print(s)
#	print()

	inc(x,y)
end=time.clock()
print(end-start)
exit(0)	
'''



def parse(x,y):
	n=len(x)
	i=0
	while(i<n):
		if(y[i]>1):
			y[i]//=2
			i+=1
			continue

		else:
			x.pop(i)
			y.pop(i)
#			i-=1
			n-=1

'''
x=[2,3,5,7,11]
y=[6,5,0,3,1]
parse(x,y)
print(x)
print(y)
exit(0)
'''
def power(a,b):
	s=1
	for i in range(0,len(a)):
		s*=a[i]**b[i]
	return s
'''
print(power([2,3,5,7],[2,3,0,1]))
exit(0)
'''
def cbrt(x):
	y=1
	while True:
		z=y-((y**3-x)/(3*y*y))
		if(z==y):
			break
		y=z
#		print(y)
	return y;
'''
print(primefac(108864))
exit(0)
'''
#cbrt(860000000)
#exit(0)
limit=110000000
count=0
m=1
while m<(limit+2)/6:
	n=m*m*(8*m-3)
	a=3*m-1
	l=primefac(n)
	x=l[0]
	# print(x)
	y=l[1]
	# print(y)
	p=1
	parse(x,y)
	for i in y:
		p*=(i+1)

	foo=[0]*len(y)
	# print(foo)
	for i in range(0,p):
		b=power(x,foo)
		c=n//(b*b)
		if(a+b+c<=limit):
#			if(a%1000==0):
			print(m,"...",a,b,c)
			count+=1
		else:
			print(m,"...",a,b,c,"=",a+b+c)

		# print(foo)
		# print(y)
		# input()
		if(len(foo)>0):
			inc(foo,y)	
		else:
			break
	print("Count so far : ",count)
	input()

	m+=1

print(count)

'''
	b=1
	while a+b<=lim:
		if(n/(b*b)==n//(b*b) and a+b+n//(b*b)<=lim):
			c=n//(b*b)
			print(m,"...",a,b,c)
			count+=1
#			input()
		b+=1
	input()
'''
