import math

def ispent(x):
	return int((1+math.sqrt(1+24*(x)))/6)==(1+math.sqrt(1+24*(x)))/6

def issumpent(m,n):
	return ispent((3*(m*m+n*n)-(m+n))/2)

def isdiffpent(m,n):
	return ispent((3*(m*m-n*n)-(m-n))/2)

def pent(x):
	return x*(3*x-1)//2

for i in range(2,100000):
	for j in range(1,i):
		if(issumpent(i,j) and isdiffpent(i,j)):
			print(i,":",pent(i))
			print(j,":",pent(j))
			print()