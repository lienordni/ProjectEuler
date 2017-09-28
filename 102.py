import math

qwe=open("./102.txt",'r')

def two_point_equation(p1,p2):
	return [p2[1]-p1[1],p1[0]-p2[0],p1[0]*p2[1]-p1[1]*p2[0]]

def slope_point_equation(p,m):
	return [m,-1,m*p[0]-p[1]]

def solve(e1,e2):
	a,b,e=e1[0],e1[1],e1[2]
	c,d,f=e2[0],e2[1],e2[2]
	return [(e*d-b*f)/(a*d-b*c),(a*f-e*c)/(a*d-b*c)]

def area(x,y):
	return (math.fabs((x[0]-x[2])*(y[1]-y[0])-(x[0]-x[1])*(y[2]-y[0])))/2

count=0
for n in range(0,1000):
	p=qwe.readline().split(',')
	p.pop()
	for i in range(0,6):
		p[i]=int(p[i])

	x=[]
	y=[]

	i=0
	while i<=5:
		x.append(p[i])
		y.append(p[i+1])
		i+=2

	print(x,y)

	A=area(x,y)
	a1=area([0,x[0],x[1]],[0,y[0],y[1]])
	a2=area([0,x[1],x[2]],[0,y[1],y[2]])
	a3=area([0,x[2],x[0]],[0,y[2],y[0]])

	if a1+a2+a3==A:
		count+=1
		print("Inside")

	else:
		print("Outside")
	# input()



print(count)

