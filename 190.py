import math

def fact(x):
	return math.factorial(x)

def superfact(x):
	p=1
	for i in range(1,x+1):
		p*=fact(i)
	return p

def p(m):
	u=2/(m+1)
	return int(u*(1-u**m)*((fact(m))**m)/((1-u)*(superfact(m))))


s=0
for i in range(2,16):
	print(i,p(i))
	s+=p(i)

print(s)

