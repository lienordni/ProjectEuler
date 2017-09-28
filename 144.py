import math

pi=3.1415926535898

error=0.0001

def next(a, b, q0, q1):
	t0=q0*pi/180
	t1=q1*pi/180
	m1 = b*(math.sin(t1)-math.sin(t0))/(a*(math.cos(t1)-math.cos(t0)))
	th1 = math.atan(m1)
	thm = math.atan((-b)*math.cos(t1)/(a*math.sin(t1)))
	m2 = -math.tan(th1-2*thm)
	x0=a*math.cos(t1)
	y0=b*math.sin(t1)

	alpha=y0-m2*x0
	gamma=b*b+a*a*m2*m2
	delta=2*a*a*m2*alpha
	epsilon=a*a*alpha*alpha-a*a*b*b

	r1=((-delta)+math.sqrt(delta*delta-4*gamma*epsilon))/(2*gamma)
	r2=((-delta)-math.sqrt(delta*delta-4*gamma*epsilon))/(2*gamma)
	if(math.fabs(x0-r1)<=error):
		X=(r2)
	else:
		X=(r1)

	alpha=1/m2
	beta=x0-y0/m2
	gamma=a*a+alpha*alpha*b*b
	delta=2*alpha*beta*b*b
	epsilon=b*b*(beta*beta-a*a)

	r1=((-delta)+math.sqrt(delta*delta-4*gamma*epsilon))/(2*gamma)
	r2=((-delta)-math.sqrt(delta*delta-4*gamma*epsilon))/(2*gamma)
	if(math.fabs(y0-r1)<=error):
		Y=(r2)
	else:
		Y=(r1)


	if(X/a>1):
		t=0

	elif(X/a<-1):
		t=pi

	elif(Y/b>1):
		t=pi/2

	elif(Y/b<-1):
		t=3*pi/2

	elif(math.fabs(X/a)<=error):
		if(Y/b>0):
			t=(pi/2)
		else:
			t=(3*pi/2)
	
	elif(X/a>0):
		if(math.fabs(Y/b)<=error):
			t=0
		elif(Y/b>0):
			t=math.cos(X/a)
		else :
			t=2*pi-math.cos(X/a)
	


	else:
		if(math.fabs(Y/b)<=error):
			t=pi
		elif(Y/b>0) :
			t=pi-math.sin(Y/b)
		else :
			t=pi+math.cos(-X/a)
		
	return t*180/pi


print(next(5,10,90,0.03))