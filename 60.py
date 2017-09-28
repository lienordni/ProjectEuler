def iridium(n): # Awesome Function
	if(n<2047):
		return [2]
	if(n<1373653):
		return [2,3]
	if(n<9080191):
		return [31,73]
	if(n<25326001):
		return [2,3,5]
	if(n<4759123141):
		return [2,7,61]
	if(n<1122004669633):
		return [2,13,23,1662803]
	if(n<2152302898747):
		return [2,3,5,7,11]
	if(n<3474749660383):
		return [2,3,5,7,11,13]
	if(n<341550071728321):
		return [2,3,5,7,11,13,17]

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def lienprime(n): # Needs iridium() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	
	for a in iridium(n):
		x=power_modulo(a,d,n)
		if(x==1):
			continue
		over=False
		for r in range(0,s):
			if(x==n-1):
				over=True
				break
			x=(x*x)%n

		if(over):
			continue

		return False

	return True

def lien(x): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

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

def ispr(x): # Needs setprimes(), contain(), prime[]
	if(x<=1):
		return False
	return (contain(x,prime))

def intersection(a,b):
	return list(set(a) & set(b))


# print(intersection([1,3,5,6,7,9,0],[2,4,5,6,7,9]))

def yes(a,b):
	return (lienprime(antilien(lien(a)+lien(b))) and lienprime(antilien(lien(b)+lien(a))))

setprimes(100000)

def lienlist(p):
	l=[]
	for i in prime:
		if yes(p,i):
			l.append(i)
	return l

# print(lienlist(3))
# exit()

p=[0]*5
for i in range(1,9587):
	p[0]=prime[i]
	l1=lienlist(prime[i])
	for j in l1:
		p[1]=j
		l2=intersection(l1,lienlist(p[1]))
		for k in l2:
			p[2]=k
			for l in range(k+1,9591):
				if yes(prime[l],prime[i]) and yes(prime[l],prime[j]) and yes(prime[l],prime[k]):
					p[3]=prime[l]
					for m in range(l+1,9592):
						if yes(prime[m],prime[i]) and yes(prime[m],prime[j]) and yes(prime[k],prime[m]) and yes(prime[m],prime[l]):
							p[4]=prime[m]
							print(p,sum(p))




