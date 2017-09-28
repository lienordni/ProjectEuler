import os

def lien(x,s=None): # Needs nothing
	c=str(x)	
	li=list(c)
	for i in range(0,len(li)):
		li[i]=int(li[i])
	if s is None:
		return li
	return [0]*(s-len(li))+li

def dikhao(l,j):
	for i in range(0,3):
		if(l[i]>0):
			print(l[i],end="  ")
		else:
			print(end="   ")
	if(j<2):
		print(end="| ")
	else:
		print(end="  ")

def display(sudoku):
	for i in range(0,9):
		for j in range(0,3):
			z=sudoku[i][3*j:(3*j+3)]
			dikhao(z,j)
		print()
		if(i%3==2 and i<8):
			print("_________|__________|_________")
			print("         |          |         ")

def showindex(sudoku):
	for i in range(0,9):
		for j in range(0,9):
			print([i,j],end=" ")
			if(j%3==2):
				print(end="     ")
		print()
		if(i%3==2):
			print()
			print()

def missing(a):
	n=0
	s=0
	for i in range(1,10):
		if a[i]==False:
			n+=1
			s=i
	if(n==1):
		return s
	return 0

def solve(sudoku):
	solved=True
	for i in range(0,9):
		for j in range(0,9):
			if(sudoku[i][j]!=0):
				continue
			solved=False
			a=[0]+[False]*9
			for x in range(0,9):
				if(x==i or sudoku[x][j]==0):
					continue
				a[sudoku[x][j]]=True
			for x in range(0,9):
				if(x==j or sudoku[i][x]==0):
					continue
				a[sudoku[i][x]]=True

			u,v=(3*(i//3)),(3*(j//3))
			for x in range(u,u+3):
				for y in range(v,v+3):
					if((x==i and y==j) or sudoku[x][y]==0):
						continue
					a[sudoku[x][y]]=True
			
			sudoku[i][j]=missing(a)
	return solved





f=open("96.txt",'r')

sudoku=[]
for i in range(0,9):
	x=int(f.readline())
	sudoku.append(lien(x,9))


display(sudoku)
input()
while solve(sudoku)==False:
	display(sudoku)
	input()