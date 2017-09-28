import math

prime=[]
oddcomposite=[]

def setprimes(n):
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				continue
			else:
				continue

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if(c):
			prime.append(x)

setprimes(100000)
x=1
i=3
while x<len(prime):
	if(i==prime[x]):
		i+=2
		x+=1
	else:
		oddcomposite.append(i)
		i+=2

x=0
while(True):
	no=False;
	y=0
	while prime[y]<oddcomposite[x]:
		if math.sqrt((oddcomposite[x]-prime[y])/2)==int(math.sqrt((oddcomposite[x]-prime[y])/2)):
			print(oddcomposite[x],"= ",prime[y],"+ { 2 * (",int(math.sqrt((oddcomposite[x]-prime[y])/2)),"^ 2 ) }")
#			input()
			no=True;
			break
		y+=1
	if(no==False):
		print(oddcomposite[x])
		exit(0)


	x+=1

