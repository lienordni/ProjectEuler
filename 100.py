import math

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

a=1
b=3
while True:
	x=6*b-a-2
	a=b
	b=x
	y=(math.sqrt(2*((2*x-1)**2)-1)-(2*x-1))/2
	if y==int(y):
		y=int(y)
		print(x,y,x+y)
		# print("x = ",primefac(x))
		# print("y = ",primefac(y))
		# print("x+y = ",primefac(x+y))
		if x+y>=10**12:
			input()
