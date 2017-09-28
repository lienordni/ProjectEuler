from itertools import permutations

def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

size=5

def constant(l):
	n=size
	for i in range(0,n-1):
		if(l[i]!=l[i+1]):
			return False
	return True

def good(t):
	five=[]
	for i in range(0,size):
		five.append(t[i])

	return t[0]==min(five)

def magic(t):
	l=[]
	v=[]
	n=size
	for i in range(0,n):
		points=[i,n+i]
		if(i==n-1):
			points+=[n]
		else:
			points+=[n+i+1]
		s=0
		for p in points:
			s+=t[p]
			v+=[t[p]]
		l.append(s)

	if(constant(l)):
		return v

l=list(permutations(range(1,2*size+1)))

for tuple in l:
	if(good(tuple)):
		m=magic(tuple)
		if(m!=None):
			print(m,len(m))




