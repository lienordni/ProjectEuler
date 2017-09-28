import math

def isq(x):
	return int(math.sqrt(x))**2==x

# a=74049690

i=1
a=[2,15,104,714,4895,33552,229970,1576239,10803704,74049690]

x=2
y=15
i=3
while True:
	z=7*y-x+1
	x=y
	y=z
	print(i,z)
	i+=1
	input()
