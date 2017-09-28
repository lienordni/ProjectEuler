def decrypt(slit,key):
	out=slit
	for i in range(0,len(out)):
		out[i]=out[i]^key[i%3]
	return out

life=open("./59.txt",'r')
slit=list((life.read()).split(','))
# print(len(slit))
for i in range(0,1201):
	slit[i]=int(slit[i])
'''
print(slit)
exit()
'''
a=[97,97,97]

def spaces(string):
	c=0
	for i in range(0,len(slit)):
		if(string[i]==' '):
			c+=1
	return c


def text(slit):
	s=""
	for i in range(0,len(slit)):
		s+=chr(slit[i])
	return s

# print(text([97,100,122]))
# exit()
# '''
temp=[0]*1201
a=[103,111,100]
for i in range(0,1201):
	temp[i]=slit[i]
output=decrypt(temp,a)
print()
print(text(output))

s=0
for i in range(0,1201):
	s+=output[i]
print(s)


# '''		
