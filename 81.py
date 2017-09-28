def antilien(li): # Needs nothing
	s=0
	for i in range(0,len(li)):
		s+=li[i]*(10**(len(li)-i-1))
	return s

def minimum_path_sum(a):
	size=len(a)
	b=[[0]*size]*size
	for i in range(0,size):
		for j in range(0,size):
			if i==0 and j==0:
				b[i][j]=a[i][j]
			elif i==0:
				b[i][j]=a[i][j]+b[i][j-1]
			elif j==0:
				b[i][j]=a[i][j]+b[i-1][j]
			else:
				b[i][j]=a[i][j]+min(b[i][j-1],b[i-1][j])
	return b[size-1][size-1]

size=80
a=[[0]*size]*size
stream=open("./81.txt",'r')

for j in range(0,size):
	s=stream.readline().split(',')
	for i in range(0,size):
		s[i]=int(s[i])
	s.pop()
	a[j]=s

for i in range(0,size):
	for j in range(0,size):
		print(a[i][j],end="  ")
	print()	

print(minimum_path_sum(a))