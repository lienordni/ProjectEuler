import math
import itertools

def isprime(x):
	if(x<2):
		return False
	if(x==2 or x==3 or x==5 or x==7):
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if(x%i==0):
			return False
	return True

def antilien(li):
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s


for p in list(itertools.permutations([1,2,3,4,5,6,7])):
	xx=antilien(p)
	if(isprime(xx)):
		print(xx)
