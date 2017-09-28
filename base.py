import math

digit=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','U','V','W','X','Y','Z']
number={ '0' : 0 ,  '1' : 1 , '2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 , '7' : 7 , '8' : 8 , '9' : 9 , 'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' : 13 , 'E' : 14 , 'F' : 15 , 'G' : 16 , 'H' : 17 , 'I' : 18 , 'J' : 19 , 'K' : 20 , 'L' : 21 , 'M' : 22 , 'N' : 23 , 'O' : 24 , 'P' : 25 , 'Q' : 26 , 'R' : 27 , 'S' : 28 , 'T' : 29 , 'U' : 30 , 'V' : 31 , 'W' : 32 , 'X' : 33 , 'Y' : 34 , 'Z' : 35 }

def convert(instring,outbase,inbase=10): # Needs math, digit[], number{}
	if inbase==outbase:
		return instring
	
	if inbase!=10:
		value=0
		l=list(instring)
		for i in range(0,len(l)):
			value+=number[l[i]]*(inbase**(len(l)-i-1))
	else:
		value=int(instring)

	if outbase==10:
		return str(value)

	length=1+math.floor(math.log(value,outbase))
	i=length-1
	l=[0]*length
	s=""
	while value>0:
		l[i]=(digit[value%outbase])
		value//=outbase
		i-=1
	for i in range(0,length):
		s+=l[i]
	return s

print(convert('34871617472',21,9))

		

	