import math

def gcd(a,b):
	r=b
	s=a
	while r!=0:
		q= s//r
		t=r
		r=s-q*t
		s=t
	return s

def factors(n):
	l=[]
	for i in range(1,n+1):
		if n%i==0:
			l.append(i)
	return l

# for i in range(1,20):
# 	print(i,factors(i))
# exit()

def pir(a): # a=a0
	q=[]
	for i in factors(a):
		q+=[-i]
	q.sort()
	return q

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def f(n,x):
	a=lien(n)
	a.reverse()
	s=0
	for i in range(0,len(a)):
		s+=a[i]*(x**i)
	return s

def ir(n):
	a=n%10
	if a==0:
		return True
	l=pir(a)
	for i in l:
		if f(n,i)==0:
			return True
	return False


count=0
for i in range(1,1+10**4):
	# if ir(i):
	# 	count+=1
	# 	print(i,end="")
	# 	input()
	if f(i,-2)==0:
		print(i)
		count+=1
print(count)


