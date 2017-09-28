def lien(x): # Needs nothing
	li=list(str(x))
	for i in range(0,len(li)):
		li[i]=int(li[i])
	return li

def bouncy(n):
	if n<100:
		return False
	l=lien(n)
	x=l[0]
	inc=True
	for i in range(1,len(l)):
		if l[i]<l[i-1]:
			inc=False
	if inc:
		# print("increasing")
		return False
	x=l[0]
	dec=True
	for i in range(1,len(l)):
		if l[i]>l[i-1]:
			dec=False
	if dec:
		# print("decreasing")
		return False
	# print("bouncy")
	return True

count=0
i=1
ratio=0.99
while True:
	print(i,end="  ")
	if bouncy(i):
		count+=1
	r=count/i
	print(r)
	if r>=ratio:
		input()
		break
	i+=1



