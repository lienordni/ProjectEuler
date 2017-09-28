import math

array=[1]*2+[-1]*10**5

def pent(k):
	return (k*(3*k-1))//2

def partitions(n): # Needs array[], pent(), math
	if n<0:
		return 0
	if array[n]!=-1:
		return array[n]
	kmin=math.ceil((1-math.sqrt(1+24*n))/6)
	kmax=math.floor((1+math.sqrt(1+24*n))/6)
	k=kmin
	s=0
	while k<=kmax:
		p=partitions(n-pent(k))
		if(k%2==1):
			s+=p
		else:
			s-=p
		k+=1
		if k==0:
			k+=1
	array[n]=s
	return s

print(partitions(5))