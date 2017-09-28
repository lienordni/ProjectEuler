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

def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def beeg(n):
	s=0
	for i in lien(n):
		s+=i*i
	return s

a=[37,58,89,145,42,20,4,16,37]
c=0
for i in range(1,1+10**7):
	n=i
	while True:
		n=beeg(n)
		if contain(n,a):
			# print(i,89)
			break
		if n==1:
			print(i)
			c+=1
			break
print(10**7-c)

