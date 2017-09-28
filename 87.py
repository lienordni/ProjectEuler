def position(x,l): # Needs nothing
	if(len(l)==0):
		return 0
	if(l[-1]<x):
		return len(l)
	if(len(l)==1 and l[0]==x):
		return 0
	low=0
	high=len(l)-1
	if(x==l[low]):
		return low+1
	if x==l[high]:
		return high+1
	if(x<l[low] or x>l[high]):
		return 0
	while True:
		mid=(low+high)//2
		if(mid==low):
			return mid+1

		if(x>l[mid]):
			low=mid
			continue
		elif(x<l[mid]):
			high=mid
			continue
		else:
			return mid+1
			
# l=[i**2 for i in range(1,15)]
# print(l)

# for i in range(0,105):
# 	print(i,position(i,l))

def f(n,s,c=None,q=None):
	if c==None and q==None:
		# print("Both are None ; Returning :",position(n,s))
		return position(n,s)

	w=0
	
	if q==None:	
		for i in range(0,position(n,c)):
			w+=f(n-c[i],s)
		# print("q is None ; Returning :",w)
		return w

	else:
		# print(n,q,position(n,q))
		for i in range(0,position(n,q)):
			w+=f(n-q[i],s,c)
		# print("Nothing is None ; Returning :",w)
		return w

def fuck(n):
	return f(n,squares,cubes,quads)

prime=[]

def setprimes(n): # Needs prime[]
	life=open("./primes1.txt","r")
	x=0
	while True:
		x=int(((life.readline()).split(", "))[1])
		if x>n:
			return
		prime.append(x)

setprimes(100100)
squares=[]
cubes=[]
quads=[]

limit=50*(10**6)

for p in prime:
	if p**2<=limit:
		squares.append(p**2)
	if p**3<=limit:
		cubes.append(p**3)
	if p**4<=limit:
		quads.append(p**4)

l=[]
for s in squares:
	for c in cubes:
		for q in quads:
			l.append(s+c+q)

l.sort()
a=(position(limit,l))

count=0
for i in range(1,a+1):
	if l[i]==l[i-1]:
		print(l[i])
		count+=1

print(a-count)