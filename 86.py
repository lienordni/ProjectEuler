import math

def distance(a,b,c):
	return math.sqrt(a**2+(b+c)**2)

def sos(a,s):
	return math.sqrt(a**2+s**2)

C=[-1]*10001
def count(m):
	if(C[m]!=-1):
		return C[m]
	x=0
	for a in range(1,m+1):
		# print(a)
		for s in range(2,2*a+1):
			y=sos(a,s)
			if(y==int(y)):
				if s>a:
					x+=(1+a-math.ceil(s/2))
					# print(a,(1+a-math.ceil(s/2)))
				else:
					x+=(s//2)
					# print(a,s//2)

	C[m]=x
	return x

low=1000
high=2000
x=(low+high)//2
while True:
	c=count(x)
	print(x,c)
	if c==10**6 or high-low<2:
		print(x,count(x))
		break
	elif c>10**6:
		high=x
		print("TOO HIGH")
	else:
		low=x
		print("TOO LOW")
	x=(low+high)//2
	print(x)

