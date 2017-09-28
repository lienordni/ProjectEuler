import time

def mediant(l1,l2):
	return [l1[0]+l2[0],l1[1]+l2[1]]

def farey(n,l1=[0,1],l2=[1,1]): # Returns Farey Sequence of order n between the fractions l1 and l2 # Needs mediant()
	[a,b]=l1
	[c,d]=l2
	f=[l1,l2]
	while True:
		i=len(f)-1
		change=False
		while i>0:
			if(mediant(f[i],f[i-1])[1]<=n):
				f.insert(i,mediant(f[i],f[i-1]))
				change=True
			i-=1
		if(change==False):
			return f

def farey2(n): # Prints Farey Sequence of order n # Needs nothing
	a,b,c,d=0,1,1,n
	while c<=n:
		k=(n+b)//d

		a,b,c,d=c, d, k*c-a, k*d-b

		# a=c
		# b=d
		# c=k*c-a
		# d=k*d-b

		# print([a,b],end=" ")


limit=8000
start=time.time()
farey2(limit)
end=time.time()
print(end-start)

