def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def stannum(n,s,m):
	a=[1]+[0]*s
	for c in n:
		for num in [s-c-i for i in range(0,s-c+1)]:
			if a[num]>0:
				a[num+c]+=a[num]
				if(a[num+c]>m):
					a[num+c]%=m
	return a[s]


f=open("250.txt",'w')
a=[]
for i in range(1,250251):
	x=power_modulo(i,i,250)
	a.append(x)
	f.write(str(x))
	f.write('\n')
# exit(0)
'''
print(stannum(a,10**9,10))
exit(0)
'''
m=10**16
s=0
for i in range(1,250):
	x=stannum(a,250*i,m)
	print(x)
	s=(s+x)%m
	print(s)
	print()