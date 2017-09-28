import math

def lienordni(n,r):
	return list(range(math.ceil(-n/r),1+math.floor((9-n)/r)))

for i in range(0,10):
	x=1
print(i)