m=0
cm=0
for x in range(2,100001):
	print(x," : ",end="")
	c=x;
	while c%2==0:
		c/=2
	while c%5==0:
		c/=5
	if c==1:
		print("Non-recurring")
		continue
	n=1
	rem=1;
	while True:
		rem*=10%c
		rem%=c
		if(rem==1):
			break
		n+=1
	if n>m:
		m=n;
		cm=c;
	print(n)
	
	

print(cm,m)
