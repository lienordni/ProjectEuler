import math
import sys

def primefac(n): # Needs math
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

def perfect_square(n):
	x=int(math.sqrt(n))
	return x*x==n

def on_circle(x,y,n):
	return ((x*x+y*y)==(n*(x+y)))

def lattice_points(n):
	l=[]
	y=n+1
	while(True):
		d=n*n+4*y*n-4*y*y
		if(d<0):
			break

		if(perfect_square(d)==False):
			y+=1
			continue

		if(d%2==n%2):
			x=(n+int(math.sqrt(d)))//2
			l.append([x,y])
			if(on_circle(x,y,n)==False):
				print("FUUUUUUUUUUUUUUUUUUUUCK")
				input()
		y+=1

	return l

def f(n):
	return 4+8*(len(lattice_points(n)))

def now(n):
	count=0
	for x in range(0,n):
		# if(n-x*x<=x*x):
		# 	break
		if perfect_square(2*n*n-x*x):
			count+=1
	return count


# for i in range(1,101):
# 	print(i,now(i))
# 	input()

# exit()

def power(a,b,m=None): # = product(a[i]**b[i]) # Needs Nothing
	if m==None:
		s=1
		for i in range(0,len(a)):
			s*=a[i]**b[i]
		return s

	s=1
	for i in range(0,len(a)):
		s*=(a[i]%m)**b[i]
		s%=m
	return s

def lien(x,size): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return ([0]*(size-len(li)))+li

digit=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','U','V','W','X','Y','Z']
number={ '0' : 0 ,  '1' : 1 , '2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 , '7' : 7 , '8' : 8 , '9' : 9 , 'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' : 13 , 'E' : 14 , 'F' : 15 , 'G' : 16 , 'H' : 17 , 'I' : 18 , 'J' : 19 , 'K' : 20 , 'L' : 21 , 'M' : 22 , 'N' : 23 , 'O' : 24 , 'P' : 25 , 'Q' : 26 , 'R' : 27 , 'S' : 28 , 'T' : 29 , 'U' : 30 , 'V' : 31 , 'W' : 32 , 'X' : 33 , 'Y' : 34 , 'Z' : 35 }

def convert(temp,outbase,inbase=10): # Needs math, digit[], number{}
	instring=str(temp)
	if inbase==outbase:
		return instring
	
	if inbase!=10:
		value=0
		l=list(instring)
		for i in range(0,len(l)):
			value+=number[l[i]]*(inbase**(len(l)-i-1))
	else:
		value=int(instring)

	if outbase==10:
		return str(value)

	length=1+math.floor(math.log(value,outbase))
	i=length-1
	l=[0]*length
	s=""
	while value>0:
		l[i]=(digit[value%outbase])
		value//=outbase
		i-=1
	for i in range(0,length):
		s+=l[i]
	return int(s)


'''
p=[5,13,17,29,37,41,53,61,73] #,89,97,101,109,113,137,149,157,173,181,193,197,229,233,241,257,269,277,281,293,313,317,337,349,353,373,389,397,401,409,421,433,449,457,461,509,521,541,557,569,577,593,601,613,617]

p.reverse()
base=4

for i in range(1,base**(len(p))):
	w=(lien(convert(i,base),len(p)))
	if(sum(w)>6):
		continue
	number=power(p,w)
	that=now(number)
	if(that==52):
		print(number, that, primefac(number))
		# input()



exit()
'''

z=int(sys.argv[1])
for i in range(z,1000100000000):
	# a=len(lattice_points(i))
	b=now(i)
	print(i,b,primefac(i))
	if(b>=13):
		input()