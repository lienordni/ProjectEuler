import math

def opp(a,b):
	return math.sqrt(a*a+b*b-a*b)	

def semiperimeter(a,b,c=None):
	if c==None:
		c=math.sqrt(a*a+b*b-a*b)
	return (a+b+c)/2

def area(a,b,c=None):
	if c==None:
		c=math.sqrt(a*a+b*b-a*b)
	s=semiperimeter(a,b,c)
	return math.sqrt(s*(s-a)*(s-b)*(s-c))

def r(a,b,c=None):
	if c==None:
		c=math.sqrt(a*a+b*b-a*b)
	return (area(a,b,c))/semiperimeter(a,b,c)


limit=10500
count=0
for a in range(1,limit+1):
	for b in range(1,a):
		# if(a==b):
		# 	continue
		ir=r(a,b)
		if ir<=100 and opp(a,b)==int(opp(a,b)):
			print(count,a,b,ir)
			count+=1
print(count)
