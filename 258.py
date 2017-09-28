def multiply(a,b):
	n=len(a)
	l=[]
	for i in range (0,n):
		l.append([0]*n)
	# print(l)
	for i in range(0,n):
		for j in range(0,n):
			s=0
			for k in range(0,n):
				# print(i,j,a[i][k],b[k][j],a[i][k]*b[k][j])
				s+=a[i][k]*b[k][j]
				# print(s)
			# print("NOW")
			l[i][j]=s
			# print(i,j,s)
			# print(l)
	return l

def power(m,e):
	n=len(m)
	if e==0:
		i=[]
		for k in range(0,n):
			i.append([0]*k+[1]+[0]*(n-k-1))
		return i
	if e==1:
		return m

	if e%2==0:
		x=power(m,e//2)
		return multiply(x,x)
	return multiply(m,power(m,e-1))

def display(matrix):
	n=len(matrix)
	for i in range(0,n):
		for j in range(0,n):
			if matrix[i][j]!=0:
				print(matrix[i][j],end="  ")
			else:
				print(end="   ")

		print()

A=[]
for i in range(0,9):
	A.append([0]*(i+1)+[1]+[0]*(8-i))
A.append([1,1]+[0]*8)

for i in range(1,301):
	print(i)
	display(power(A,i))
	print("________")
	input()

