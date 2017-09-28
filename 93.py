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

def fuck(a):
	l=int(len(a))
	b=[]
	for i in a:
		if i>=0 and i==int(i):
			b.append(int(i))
	b.sort()
	i=0
	l=len(b)
	while i < l-1:
		if b[i]==b[i+1]:
			b.pop(i)
			l-=1
		else:
			i+=1
	return b

def reachable(l):
	if len(l)==1:
		return [l[0]]
	if len(l)==2:
		a,b=l[0],l[1]

		return [a+b,a-b,b-a,a*b,a/b,b/a]
	# if len(l)==3:
	a=[]
	for i in l:
		vishal=list(l)
		vishal.remove(i)
		lienordni=reachable(vishal)
		for shit in lienordni:
			a+=reachable([i,shit])
	return a

print(fuck(reachable([1,2,3])))





