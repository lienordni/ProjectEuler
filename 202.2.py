def cunt(q,b): # Returns number of odd multiples of q, that are less than b/3
	x=(b/3)/q
	if(x==int(x)):
		return (int(x)-1)//2
	return (int(x)+1)//2

def binary(i,size=None):
	s=bin(i)
	lol=[int(x) for x in s[2:]]
	if(size!=None):
		lol=[0]*(size-len(lol))+lol
	return lol

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
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def ones(y):
	c=0
	for i in y:
		if(i==1):
			c+=1
	return c

'''
print(ones([1,0,0,1,0,1,1,1,0,1,0,0,0,1,1]))
exit()
'''

def product(y,facts):
	s=1
	for i in range(0,len(y)):
		if y[i]==1:
			s*=facts[i]
	return s

'''
print(product([1,0,0,1,1],[3,5,7,11,13]))
print(3*11*13)
exit()
'''

def beta(b):
	x=(b/3)
	if(x==int(x)):
		return (int(x)-1)//2
	return (int(x)+1)//2

def lienordni(a):
	facts=primefac(a)[0]
	# print(facts)
	num=len(facts)
	s=0
	for x in range(1,2**num-1):
		y=binary(x,num)
		# print(facts)
		# print(product(y,facts))
		# print(y)
		if ones(y)%2==1:
			s+=cunt(product(y,facts),a)
			# print("+= cunt(",product(y,facts),",",a,") = ",cunt(product(y,facts),a))
		else:
			s-=cunt(product(y,facts),a)
			# print("-= cunt(",product(y,facts),",",a,") = ",cunt(product(y,facts),a))
	return 2*(beta(a)-s)

# print(6008819575-3*(6008819575//3))

n=int(input())
print(lienordni(n))
