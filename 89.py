def simp(a): # Needs nothing
	i=0
	l=len(a)
	if l==1:
		return a
	while True:
		if i>=l-1:
			break
		# print(i,l)
		if a[i]<a[i+1]:
			a[i]=a[i+1]-a[i]
			a.pop(i+1)
			l-=1
		i+=1
		# print(a)
	return a

def decimal(s): # Converts Roman Numerals to Decimal # Needs simp()
	n=0
	a=[]
	for i in list(s):
		if(i=='M'):
			a.append(1000)

		elif(i=='D'):
			a.append(500)

		elif(i=='C'):
			a.append(100)

		elif(i=='L'):
			a.append(50)

		elif(i=='X'):
			a.append(10)

		elif(i=='V'):
			a.append(5)

		else:
			a.append(1)

	return sum(simp(a))


def roman(n): # Converts Decimal to Roman Numerals
	if n==0:
		return ""
	if n==1000:
		return "M"

	if n==500:
		return "D"

	if n==100:
		return "C"

	if n==50:
		return "L"

	if n==10:
		return "X"

	if n==5:
		return "V"

	if n==1:
		return "I"

	if n>1000:
		return "M"*(n//1000)+roman(n%1000)

	if n>=900:
		return "CM"+roman(n%100)

	if n>500:
		return "D"+roman(n%500)

	if n>=400:
		return "CD"+roman(n%100)

	if n>100:
		return "C"*(n//100)+roman(n%100)

	if n>=90:
		return "XC"+roman(n%10)

	if n>50:
		return "L"+roman(n%50)

	if n>=40:
		return "XL"+roman(n%10)

	if n>10:
		return "X"*(n//10)+roman(n%10)

	if n==9:
		return "IX"

	if n>5:
		return "V"+"I"*(n%5)

	if n==4:
		return "IV"

	return "I"*n


qwe=open("./89.2.txt",'r')
array=[""]+(qwe.read()).split('\n')

rty=open("/home/lienordni/Desktop/Code/ProjectEuler/89.txt",'r')
random=(rty.read()).split('\n')

uio=open("/home/lienordni/Desktop/Code/ProjectEuler/89.3.txt",'r')
num=[]
m=0
for i in range(0,1000):
	q=int(uio.readline())
	num.append(q)

s=0
for i in range(0,1000):
	s+=len(random[i])-len(roman(num[i]))

print(s)
	

