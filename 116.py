size=50
a=1
b=1
for i in range(2,size+1):
	c=a+b
	a=b
	b=c
	# print(i,c)
s=0
print("Red =",c-1)
s+=c-1
a=b=c=1

for i in range(3,size+1):
	d=a+c
	a=b
	b=c
	c=d
	# print(i,d)

print("Green =",d-1)
s+=d-1
a=b=c=d=1

for i in range(4,size+1):
	e=a+d
	a=b
	b=c
	c=d
	d=e
	# print(i,e-1)

print("Blue ",e-1)
s+=e-1
print("Sum =",s)

