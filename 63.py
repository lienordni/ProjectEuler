import math

n=0

for d in range(1,23):
	l=math.ceil(10**((d-1)/d))
	print(d,l)
	n+=10-l
print(n)
