def g(a,b):
	if a==b:
		return 0
	return 1

F=[[False,True]]*2+[[True,False]]*2+[[True,True]]+[[False,False]]*1000

def debug(x,y):
	if(x==[False,True]):
		print("L",end=" ")

	elif(x==[True,True]):
		print("WL",end=" ")

	else:
		print("W",end=" ")
	print(end=": ")
	if(y==[False,True]):
		print("L",end=" ")

	elif(y==[True,True]):
		print("WL",end=" ")

	else:
		print("W",end=" ")
	print(end="  = ")

def f(n):
	if(F[n]!=[False,False]):
		return F[n]

	b=[False,False]
	for i in range(0,n//2):
		x=f(i)
		y=f(n-i-2)
		print(i,":",n-i-2,end="  =  ")
		debug(x,y)
		a=g(x,y)
		if(a==1):
			print("L")
		else:
			print("W")
		b[a]=True
		# if b[1-a]==True:
		# 	break
	F[n]=b
	return b

def debug2(x):
	if(x[0]):
		print("W",end="")

	if(x[1]):
		print("L",end="")

for i in range(0,1000):
	x=f(i)
	print(i,end=" = ")
	debug2(x)
	print()

	input()