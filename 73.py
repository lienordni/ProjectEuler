import math

def gcd(a,b): # Copied From Wikipedia, No fucking idea how it works.
	r=b
	old_r=a
	while r!=0:
		quotient= old_r//r

		prov=r
		r=old_r-quotient*prov
		old_r=prov

	return old_r

def mediant(l1,l2):
	return [l1[0]+l2[0],l1[1]+l2[1]]

def farey(n,l1=[0,1],l2=[1,1]): # Returns Farey Sequence of order n between the fractions l1 and l2 # Needs mediant()
	[a,b]=l1
	[c,d]=l2
	f=[l1,l2]
	s=0
	while True:
		i=len(f)-1
		change=False
		while i>0:
			if(mediant(f[i],f[i-1])[1]<=n):
				f.insert(i,mediant(f[i],f[i-1]))
				s+=1
				change=True
			i-=1
		if(change==False):
			return s

# print(farey(20))
# exit()

def count(lim):
	s=0
	for d in range(5,lim+1):
		x=math.ceil(d/3)
		y=math.floor(d/2)
		for i in range(x,y+1):
			if gcd(i,d)==1:
				# print([i,d])
				s+=1
	return s


# print(farey(30,[1,3],[1,2]))
print(count(12000))

