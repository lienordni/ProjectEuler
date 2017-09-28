import math

for a in range(-10,21):
	for b in range(-10,151):
		x=math.sqrt(a*a+4*b)
		if x==int(x):
			print(a,b)

	print()