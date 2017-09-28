def lien(x): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def convergent(cf): # Needs Nothing
	A=cf[0]
	a=cf[1]
	n=len(a)
	p=1
	q=a[n-1]
	for i in range(1,len(a)):
		pn=q
		qn=a[n-1-i]*q+p
		p=pn
		q=qn
	return [q*A+p,q]

print(sum(lien(6963524437876961749120273824619538346438023188214475670667)))
a=[]
for i in range(0,99):
	if(i%3==1):
		a.append(2*(1+i//3))
	else:
		a.append(1)
print(convergent([2,a]))
