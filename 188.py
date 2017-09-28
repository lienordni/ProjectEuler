x=3
c=int(x)
y=7
i=1
'''
while True:
	if x==c%y:
		input()
	print(i,x%y)
	x*=c
	x%=y
	i+=1
'''
k=[10**8,1250000,62500,12500,2500,500,100,20,4,1,0]

x=1777

y=(x**k[10])%(k[8])
i=7
while i>=0:
	y=(x**y)%(k[i])
	print(y)
	i-=1

