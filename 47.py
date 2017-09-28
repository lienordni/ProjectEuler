def primefac(n):
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

def distinct(a,b):
	a.sort()
	b.sort()
	i,j=0,0
	while i<len(a) and j<len(b):
		if(a[i]==b[j]):
			return False
		elif(a[i]<b[j]):
			i+=1
		else:
			j+=1
	return True

def megadistinct(L):
	for i in range(0,len(L)-1):
		if(distinct(L[i],L[i+1])==False):
			return False
	return True

size=int(input())

'''
i=2
while True:
	if(megadistinct([primefac(i+n)[0] for n in range(0,size)])):
		print([n for n in range(i,i+size)])
		input()
	i+=1
'''
#print(megadistinct([[2],[3],[2]]))

x=2
while True:
	l=[]
	if(x%100==0):
		print(x)
	fuck_this_shit=False
	for i in range(x,x+size):
		y=primefac(i)[0]
		if(len(y)!=size):
			fuck_this_shit=True
			break
		l.append(y)
	if(fuck_this_shit):
		x+=1
		continue
	if(megadistinct(l)):
		print([n for n in range(x,x+size)])
		input()
	x+=1