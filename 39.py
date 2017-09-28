import math

p=[0]*1001
for c in range(2,1001):
	for a in range(1,int(math.sqrt(c*c/2)+1)):
		b=math.sqrt(c*c-a*a)
		if(b==int(b) and a+b+c==840):
			b=int(b)
			print(a,b,c)
			p[a+b+c]+=1

exit(0)
max=0
pmax=0
for i in range(0,1001):
	if(p[i]>max):
		max=p[i]
		pmax=i
		print(i,p[i])
		# input()

print("ans = ",pmax)