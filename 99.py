import math

stream=open("99.txt","r")
m=0
im=0
for i in range(1,1001):
	nums=stream.readline()
	l=nums.split(',')
	l[1]=l[1][:len(l[1])-1]
	l[0]=int(l[0])
	l[1]=int(l[1])
	print(l,"=",l[1]*math.log10(l[0]))
	if(l[1]*math.log10(l[0])>m):
		m=l[1]*math.log10(l[0])
		im=i

print(im,m)
