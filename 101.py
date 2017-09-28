def function(n):
	return (1+n**11)//(1+n)
	# return n**3

def interpolation(x,y,xn): # x and y are arrays. # Returns the y element corresponding to xn
	s=0
	n=len(x)
	for i in range(0,n):
		p=y[i]
		for j in range(0,n):
			if j==i:
				continue
			p*=(xn-x[j])/(x[i]-x[j])
		s+=p
	if s==int(s):
		return int(s)
	return s


degree=10
array=[]

for i in range(1,degree+2):
	array.append(function(i))

# print(array)
s=0
for k in range(1,degree+1):
	s+=(interpolation([i for i in range(1,len(array[:k])+1)],array[:k],len(array[:k])+1))
print(s)


