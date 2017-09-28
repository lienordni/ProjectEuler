def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

l=[]
i=1
d=1
while len(l)<=10**6:
	l+=(lien(i))
	i+=1

'''
for i in range(0,100):
	print(i+1,l[i])
	input()
'''
for i in range(0,7):
	print(l[10**i-1])
