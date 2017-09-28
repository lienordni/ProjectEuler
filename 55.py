'''
def lien(x):
	
	c=str(x)
	li=[]
	for i in range(0,len(c)):
		li.append(int(c[i])
#	print(type(li))
'''
#lien(1826)
def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def palin(n):
	l=lien(n)
	for i in range(0,len(l)//2):
		if(l[i]!=l[len(l)-i-1]):
			return False
	return True
	
def morph(x):
	l=lien(x)
	s=len(lien(x))
	n=0
	for i in range(0,s):
		n+=l[i]*(10**i)
	return n+x

count=0
for i in range(1,10001):
	x=morph(i)
	bla=True
	for c in range(0,52):
#		print(x)
#		input()
		if palin(x):
			bla=False
			break
		x=morph(x)
	if(bla):
		print(i,end='')
		input()
		count+=1

print(count)
