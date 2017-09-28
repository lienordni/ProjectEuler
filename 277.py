import math
def func(x,s):
	l=list(s)
	l.reverse()
	y=x
	for c in l:
		if c=='D':
			y*=3
		elif c=='d':
			if (3*y+1)/2!=int((3*y+1)/2):
				return "FUCK"
			y=(3*y+1)//2
		else:
			if (3*y-2)/4!=int((3*y-2)/4):
				return "FUCK"
			y=(3*y-2)//4
	return y
s="UDDDUdddDDUDDddDdDddDDUDDdUUDd"
x=1
while True:
	f=func(x,s)
	x+=1
	if f!="FUCK":
		print(f,1+int(math.log10(f)))
		# input()
