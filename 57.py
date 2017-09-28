import math

p=1
q=1
c=0
for i in range(1,1001):
	m=p+2*q
	n=p+q
	p=m
	q=n
	print(i,":",p,"/",q,"=",p/q,end="    ")
	if(int(math.log10(p))!=int(math.log10(q))):
		print("*")
		c+=1
	else:
		print()

print(c)