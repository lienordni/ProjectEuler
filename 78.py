import math
import time
array=[1]*2+[-1]*10**6

def pent(k):
	return (k*(3*k-1))//2

def partitions(n): # Needs array[], pent()
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

start=time.clock()
i=1
while True:
	p=partitions(i)
	print(i,p)
	if p%(10**6)==0:
		break
	i+=1
	# input()
end=time.clock()
print(end-start)