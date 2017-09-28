F=[-1]*51

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

print(f(50,3))