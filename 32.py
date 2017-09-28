import math

def pan(l):
	if(len(l)!=9):
		return False
	l.sort()
	if(l==[1,2,3,4,5,6,7,8,9]):
		return True
	return False

def lsit(x):
	l=[]
	c=x
	while c>0:
		l.append(c%10)
		c//=10
	return l

def pna(a,b,c):
	l=[]
	l=lsit(a)+lsit(b)+lsit(c)
	return pan(l)

def lien(x):
	l=sorted(lsit(x))
	for i in range(0,len(l)-1):
		if l[i+1]==l[i]:
			return False
	return True

def s(l):
	l.sort()
	i=0
	while i<len(l)-1:
		if(l[i]==l[i+1] and 1==2):
			l.pop(i)
		else:
			i+=1

	return sum(l)

that=[]
for i in range(1000,10000):
	if lien(i)==False:
		continue
	for j in range(1,100):
		if(i%j==0):
			if(pna(i,j,i/j)):
				print(i,"=",j,"*",i//j)
				that.append(i)

print(s(that))







