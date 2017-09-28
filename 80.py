import math

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

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

def convergent(cf): # Needs Nothing
	A=cf[0][0]
	a=cf[1]
	n=len(a)
	p=1
	q=a[n-1]
	for i in range(1,len(a)):
		pn=q
		qn=a[n-1-i]*q+p
		p=pn
		q=qn
	return [q*A+p,q]

def sq_convergent(n,k): # Needs continued_fraction(), convergent()
	c=continued_fraction(n)
	x=c[0]
	r=c[1]
	p=len(r)
	if p==0:
		return
	f=x
	s=r*(k//p)+r[:(k%p)]
	# print([f,s])
	return convergent([f,s])

def recurrence_period(x): # Needs nothing # Length of repeating block of digits with given denominator
	c=x;
	while c%2==0:
		c/=2
	while c%5==0:
		c/=5
	if c==1:
		# print("Non-recurring")
		return 0
	n=1
	rem=1
	while True:
		rem*=10%c
		rem%=c
		if(rem==1):
			return n
		n+=1

def decimal_digits(f): # Needs recurrence_period() # Returns decimal expansion of rational fraction as [integer part,fractional part/recurring part,recurring??]
	a=f[0]
	b=f[1]
	c=a//b
	n=a%b
	d=n*10
	s=""
	p=recurrence_period(b)
	if p==0:
		while True:
			x=d//b
			if x==0:
				return [c,list(s),False]
			cr=d%b
			d=10*cr
			s+=str(x)
	for i in range(0,p):
		x=d//b
		cr=d%b
		d=10*cr
		s+=str(x)
	return [c,list(s),True]

'''
print(decimal_digits([17,89]))
print()
# print(recurrence_period(892734))
exit()
'''
def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s


x=open("./80.txt",'r')
y=x.read()
def sqrt_digits(n,k):
	a,b=5*n,5
	r=int(math.sqrt(n))
	accuracy=-len(lien(int(math.sqrt(n))))
	accuracy=0
	while accuracy<k:
		if a>=b:
			a-=b
			b+=10
		else:
			a*=100
			b=b*10-45
			accuracy+=1
	return (b//100)
	return antilien(lien(b//100)[(len(lien(int(math.sqrt(n))))):])

def sod(n):
	c=n
	s=0
	while c>0:
		s+=c%10
		c//=10
	return s
s=0
for i in range(2,100):
	if(int(math.sqrt(i))*int(math.sqrt(i))==i):
		continue
	print(i,sod(sqrt_digits(i,100)))
	s+=sod(sqrt_digits(i,100))
print(s)
# print(sod(sqrt_digits(2,100)))
exit()
for i in range(1,200):
	# con=sq_convergent(2,i)
	# dec=decimal_digits(sq_convergent(2,i))
	# print(i,con,p_error(y,dec[0][1],dec[1]))
	input()




