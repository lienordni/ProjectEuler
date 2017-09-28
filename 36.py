def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li):
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def palin(n):
	l=lien(n)
	for i in range(0,len(l)//2):
		if(l[i]!=l[len(l)-i-1]):
			return False
	return True
	
def binary(x):
	this=bin(x)
	that=[int(i) for i in this[2:]]
	return antilien(that)

count=0
sum=0
for i in range(1,1000001):
	if(palin(i) and palin(binary(i))):
		print(i,binary(i))
		count+=1
		sum+=i

print(count)
print(sum)