def lien(x): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def strip(x):
	y=[]
	for i in [2*x for x in range(0,len(x)%2+len(x)//2)]:
		y.append(x[i])
	return y

i=10**5
218311
while True:
	# print(i)
	if strip(lien(i*i))==[2,1,8,3,1,1]:
		print(i,i*i)
		break
	i+=1