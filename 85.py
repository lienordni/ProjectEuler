def s(m,n):
	return m*n*(m+1)*(n+1)//4

closest=[0,0]
difference=2000000
for m in range(1,501):
	for n in range(1,m+1):
		print(m,n,s(m,n))
		d=max(s(m,n),2000000)-min(s(m,n),2000000)
		if d<difference:
			closest=[m,n]
			difference=d

print(closest,s(closest[0],closest[1]))