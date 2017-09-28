import math
from decimal import *

getcontext().prec = 1000

def golden_nugget(n):
	return (Decimal(5*n*n+14*n+1).sqrt())%1==0

x=5
n=x
phi=(1+math.sqrt(5))/2
while True:
	n*=(phi**4)
	n=int(n)
	while golden_nugget(n)==False:
		n+=1
	print(n,n/x)
	x=n
	# input()