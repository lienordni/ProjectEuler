def lien(x): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def join(a,b):
	return int(str(a)+str(b))

def f(l):
	if(len(l)==2):
		a=l[0]
		b=l[1]
		return [[a*b,a/b,a+b,a-b],[join(a,b)]]

	if(len(l)==3):
		a=l[0]
		b=l[1]
		c=l[2]
		x=f([a,b])
		ans1=[]
		ans2=[]
		for i in x[0]:
			ans1+=[i*c,i/c,i+c,i-c]
		for i in x[1]:
			ans1+=[i*c,i/c,i+c,i-c]
			ans2+=[join(i,c)]
		x=f([b,c])
		for i in x[0]:
			ans1+=[a*i,a/i,a+i,a-i]
		for i in x[1]:
			ans1+=[a*i,a/i,a+i,a-i]
			ans2+=[join(a,i)]
		return [ans1,ans2]
	

print(f([1,2,3]))
		