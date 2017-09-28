a=b=c=1
n=4
m=0
mod=3
while True:
	# print(mod)
	lien=True
	a=b=c=1
	n=4
	while True:
		d=(a+b+c)%mod
		if(d==0):
			# print("zero")
			lien=False
			break
		a=b
		b=c
		c=d
		# print(n,d,mod,[a,b,c])
		n+=1
		if([a,b,c]==[1,1,1]):
			break
	# input()
	if(lien):
		m+=1
		print(m,mod)
		if(m==124):
			input()
	mod+=2