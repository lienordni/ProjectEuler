def sum(x):
	s=0
	c=x
	while c>0:
		s+=c%10
		c//=10
	return s


max=[0,0,0]
for a in range(1,100):
	for b in range(1,100):
		if(sum(a**b)>max[0]):
			max=[sum(a**b),a,b]

print(max)