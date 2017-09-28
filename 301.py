def lithium(a,b): # 2x2 Matrix Multiplication 
	return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]]

def rhenium(x,y,n=None):	# 2x2 Modular Matrix Exponentiation, Needs Lithium()
	if n is None:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			return x
		if(y%2==0):
			z=rhenium(x,y//2)
			return lithium(z,z)

		return lithium(rhenium(x,y-1,n),x)


	else:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			z=[]
			for i in range(0,4):
				z.append(x[i]%n)
			return z
		if(y%2==0):
			z=rhenium(x,y//2,n)
			p=(lithium(z,z))
			q=[]
			for i in range(0,4):
				q.append(p[i]%n)
			return q

		f=lithium(rhenium(x,y-1,n),x)
		g=[]
		for i in range(0,4):
			g.append(f[i]%n)
		return g

def fibonacci(n,m=None): #Needs lithium(), rhenium()
	a=[1,1,1,0]

	if m is None:
		b=rhenium(a,n)
	else:
		b=rhenium(a,n,m)

	return b[1]

def lien(x): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def binary(i,size=None):
	s=bin(i)
	lol=[int(x) for x in s[2:]]
	if(size!=None):
		lol=[0]*(size-len(lol))+[int(x) for x in s[2:]]
	return lol

'''
print(binary(69))
exit(0)
'''

def which(x):
	c=x
	i=-1
	# print("i",i)
	while c>0:
		c//=2
		i+=1
	return i

# print(which(1024))
# exit()

print(fibonacci(32))
exit()
array=[2**i for i in range(0,30)]
c=0
for i in range(1,10000):
	xor=i^(2*i)^(3*i)
	# print(i,end="  ")
	# print(' '*(1+len(lien(i))),binary(2*i,10))
	# print(' '*(1+len(lien(i))),binary(3*i,10))
	if xor==0:
		c+=1
		print(i,binary(i,10),c,end="   ")
		# print("xor =",xor)
		if i in array:
			print(fibonacci(which(i)+2))
			input()
		else:
			print()



