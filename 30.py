def lol(x):
	c=x
	s=0
	while c>0:
		s+=int((c%10)**5)
#		print(c%10,(c%10)**5)
#		input()
		c//=10
	if s==x:
		return True
	return False

s=0
for i in range(2,10000000):
	if lol(i):
		s+=i
		print(i,s)


