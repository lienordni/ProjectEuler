import itertools

def lien(x):
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def antilien(li):
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

prime=[2,3,5,7,11,13,17]
def loob(x):
	for i in range(1,8):
		if(antilien(x[i:(i+3)])%prime[i-1]!=0):
			return False
	return True

'''
print(loob(lien(1406357289)))
exit(0)
'''

s=0
for i in list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[362880:]:
	if(loob(i)):
		print(antilien(i))
		s+=antilien(i)
print(s)