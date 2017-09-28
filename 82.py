def liensum(a,i,j,k):
	if i==k:
		return a[i][j+1]

	s=a[k][j+1]
	if k>i:
		for n in range(i+1,k+1):
			s+=a[n][j]
		return s

	for n in range(k,i):
		s+=a[n][j]
	return s

def display(n):
	for q in range(0,size):
		for w in range(0,size):
			print(n[q][w],end="  ")
		print()	
	print()

def minpathsum(a):
	size=int(len(a))
	n=[]
	for i in range(0,size):
		n+=[[0]*size]
	# display(n)
	for j in range(1,size):
		if j==1:
			for i in range(0,size):
				n[i][1]=(a[i][1]+a[i][0])
				# display(n)
			# exit()
		else:
			for x in range(0,size):
				m=liensum(a,0,j-1,x)+n[0][j-1]
				# print(x,m-n[0][j-1])
				for y in range(1,size):
					f=liensum(a,y,j-1,x)+n[y][j-1]
					if f<m:
						m=f
				# print(x,j)
				n[x][j]=m
	q=n[0][size-1]
	for i in range(1,size):
		if n[i][size-1]<q:
			q=n[i][size-1]
	return q

size=80
a=[[0]*size]*size

stream=open("./82.txt",'r')

for j in range(0,size):
	s=stream.readline().split(',')
	for i in range(0,size):
		s[i]=int(s[i])
	s.pop()
	a[j]=s

# display(a)
print(minpathsum(a))







# stream=open("./82.txt",'r')

# for j in range(0,size):
# 	s=stream.readline().split(',')
# 	for i in range(0,size):
# 		s[i]=int(s[i])
# 	s.pop()
# 	a[j]=s

