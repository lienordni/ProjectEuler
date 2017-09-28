F=[-1]*51

def f(n):
	if n<2:
		return 1
	if n==2:
		return 2
	if F[n]!=-1:
		return F[n]
	s=1+f(n-2)+2*f(n-3)
	for k in range(0,n-3):
		s+=3*f(k)
	F[n]=s
	return s

print(f(50))