import math

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def same(x,y):
	return sorted(lien(x))==sorted(lien(y))


i=1000002
m=0
while True:
	count=0
	print(i,":")
	for x in range(i,int(10**(int(1+3*math.log10(i))/3))+1):
		if same(i**3,x**3):
			count+=1
	print(count)
	if count>m:
		m=count
		input()
	i+=1