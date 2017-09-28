F=[-1]*5100

def f(n,m):
	if m<=0:
		return 1
	if F[n]!=-1:
		return F[n]
	s=0
	for k in range(1,n-m+2):
		s+=k*f(n-m-k,m)
	F[n]=s+1
	return s+1

m=50
n=50

while True:
	x=f(n,m)
	print(n,x)
	if x>=10**6:
		input()
	n+=1



