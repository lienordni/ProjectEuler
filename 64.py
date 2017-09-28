import math

def continued_fraction(d): # Continued Fraction of sqrt(d) # Needs math
	r=int(math.sqrt(d))
	if r*r==d:
		return [[r],[]]

	a=r
	p=0
	q=1
	f=[]
	while True:
		p=a*q-p
		q=(d-p*p)//q
		a=(r+p)//q
		f.append(a)
		if q==1:
			break
	return [[r],f]

count=0
for i in range(2,10001):
	c=continued_fraction(i)
	print(i,c,len(c[1]))
	if(len(c[1])%2==1):
		count+=1
print(count)