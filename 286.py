def p(x,y,q):
	if x>y:
		return 0
	if x<0:
		return 0
	if y==1:
		if x==0:
			return 1/q
		elif x==1:
			return 1-1/q
	return p(x,y-1,q)*(x/q)+p(x-1,y-1,q)*(1-x/q)

print(p(2,5,5.00001))
