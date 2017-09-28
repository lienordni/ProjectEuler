file=open("./248.txt","r")
l=[]
i=0
while True:
	x=int(file.readline())
	if(x==-1):
		break;
	i+=1
	print(i,x)
	if(x==23507044290):
		input()
	l.append(x)
	# input()

l.sort()

print(l[-1])
