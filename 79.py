
def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

qwe=open("79.txt",'r')
x=qwe.read().split('\n')
for i in range(0,50):
	x[i]=int(x[i])

left=[]
right=[]
for i in range(0,10):
	left+=[[False]*10]
	right+=[[False]*10]

for i in range(0,50):
	l=lien(x[i])
	right[l[0]][l[1]]=True
	right[l[0]][l[2]]=True
	right[l[1]][l[2]]=True
	left[l[1]][l[0]]=True
	left[l[2]][l[0]]=True
	left[l[2]][l[1]]=True

for i in range(0,10):
	print(i,end=" : ")
	for j in range(0,10):
		if right[i][j]:
			print(j,end=" ")
	print()
