import math

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def fuck(n):
	s=0
	for i in lien(n):
		s+=math.factorial(i)
	return s


count=0
for c in range(1,1000001):
	x=c
	a=[]
	while True:
		# print(x)
		# input()
		x=fuck(x)
		if x in a:
			break
		a.append(x)
		# input()
	print(c,len(a)+1)
	if len(a)==59:
		count+=1
		# input()
	# input()

print(count)