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

def gcd(a,b):
	if a>b :
		x,y=a,b
	else:
		x,y=b,a

	if(x%y==0):
		return y
	return gcd(y,x%y)

def lienordni(n):
	i=3
	count=1
	while i<=n//3:
		if(gcd(n,i)==1):
			print(i)
			count+=1
		i+=2
	return count

n=int(input())
print(lienordni(n))