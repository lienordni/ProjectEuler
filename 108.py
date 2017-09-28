prime=[]

def setprimes(n): # Needs prime[]
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				continue
			else:
				continue

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if(c):
			prime.append(x)

def inc(x,low,up): # Increments a number array x with variable base array ranges low->up # Needs nothing
	l=len(up)
	if(x[l-1]!=up[l-1]-1):
		x[l-1]+=1
		return
	p=l-1
	while p>=0:
		if(x[p]!=up[p]-1):
			x[p]+=1
			for k in range(p+1,l):
				x[k]=low[k]
			return
		p-=1
	for i in range(0,l):
		x[i]=low[i]
	return

'''
low=[3,2,4]
up=[6,9,8]
x=[3,2,4]
while True:
	print(x)
	inc(x,low,up)
	input()
'''

'''

y=[10,10,10]
x=[0,0,0]
fart=False
while True:
	print(x)
	inc(x,y)
	input()

exit()
'''


def contain(x,l): # Needs nothing
	if(len(l)==0):
		return False
	if(len(l)==1):
		return x==l[0]
	low=0
	high=len(l)-1
	if(x==l[low] or x==l[high]):
		return True
	if(x<l[low] or x>l[high]):
		return False
	while True:
		mid=(low+high)//2
		if(mid==low):
			return False

		if(x>l[mid]):
			low=mid
			continue
		elif(x<l[mid]):
			high=mid
			continue
		else:
			return True

import math

def primefac(n): # Needs nothing
	d=2
	i=-1
	factors=[]
	indices=[]
	while(n>1):
		if(n%d==0):
			i+=1
			factors.append(d)
			indices.append(0)
		while(n%d==0):
			indices[i]+=1
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]

def gcd(a,b):
	if a>b :
		x,y=a,b
	else:
		x,y=b,a

	if(x%y==0):
		return y
	return gcd(y,x%y)
	
def diophantine(n):
	r=0
	for x in range(n+1,2*n+1):
		if (x*n)%(x-n)==0:
			# print("1 /",x,"-","1 /",n,"=",(x-n),'/',(x*n),'= 1/',(x*n)//(x-n)," "*10,"YO")
			r+=1
		# else:
		# 	g=gcd(x*n,x-n)
		# 	print("1 /",x,"-","1 /",n,"=",(x-n),"/",(x*n),'=',(x-n)//g,"/",(x*n)//g)
	return r

def power(a,b): # = product(a[i]**b[i]) # Needs Nothing
	s=1
	for i in range(0,len(a)):
		s*=a[i]**b[i]
	return s

'''
print(power([2,3,7],[3,2,1]))
exit()
'''

setprimes(41)
array=[]
# print(len(prime))
# p=[2,3,5,7,11,13]
for q in range(3,7):
	n=0
	size=1
	low=[3,2,1,1,1,1]+[1]*q
	up=[12,8,6,5,3,3]+[2]*q
	a=list(low)
	for i in range(0,len(low)):
		size*=(up[i]-low[i])
	for i in range(0,size):
		# print(a,power(prime,a))
		array.append(power(prime[:(-(7-q))],a))
		inc(a,low,up)
		# input()

m=0
i=2
hcn=[2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040,7560,10080,15120,20160,25200,27720,45360,50400,55440,83160,110880,166320,221760,277200,332640,498960,554400,665280,720720,1081080,1441440,17297280,21621600,32432400,36756720,43243200,61261200,73513440,110270160,122522400,147026880,183783600,245044800,294053760,367567200,551350800,698377680,735134400,1102701600,1396755360,2095133040,2205403200,2327925600,2793510720,3491888400,4655851200,5587021440,6983776800,10475665200,13967553600,20951330400,27935107200,41902660800,48886437600,64250746560,73329656400,80313433200,97772875200,128501493120,146659312800,160626866400,240940299600,293318625600,321253732800,481880599200,642507465600,963761198400,1124388064800,1606268664000,1686582097200,1927522396800,2248776129600,3212537328000,3373164194400,4497552259200,6746328388800,8995104518400,9316358251200,13492656777600,18632716502400,26985313555200,27949074753600,32607253879200,46581791256000,48910880818800,55898149507200,65214507758400,93163582512000,97821761637600,130429015516800,195643523275200,260858031033600,288807105787200,391287046550400,577614211574400,782574093100800,866421317361600,1010824870255200,1444035528936000,1516237305382800,1732842634723200,2021649740510400,2888071057872000,3032474610765600,4043299481020800,6064949221531200,8086598962041600,10108248702552000,12129898443062400,18194847664593600,20216497405104000,24259796886124800,30324746107656000,36389695329187200,48519593772249600,60649492215312000,72779390658374400,74801040398884800]
array.sort()
i=4
for i in array:
	x=primefac(i)
	p=1
	for a in x[1]:
		p*=(2*a+1)
	t=(p+1)//2
	if(t>1000):
		input()
	if(t>m):
		m=t
		print(i,t,x[1])
		input()
		# input()
	i+=1