import math

def tri(x):
	return (-1+math.sqrt(1+8*x))/2==int((-1+math.sqrt(1+8*x))/2)

def pent(x):
	return (1+math.sqrt(1+24*x))/6==int((1+math.sqrt(1+24*x))/6)

def hexa(x):
	return int((1+math.sqrt(1+8*x))/4)

i=2
while True:
	if(pent(i*(2*i-1)) and tri(i*(2*i-1))):
		print(i*(2*i-1))
		print()
	i+=1