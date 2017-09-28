import math
def c(n,r):
	return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

count=0
for n in range(20,101):
	for r in range(0,n+1):
		if(c(n,r)>10**6):
			count+=1

print(count)