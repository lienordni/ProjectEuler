import math

def shit(lien):
	i=0
	while True:
		if i==len(lien)-1:
			break
		if lien[i+1]-lien[i]<=0.01:
			lien.pop(i)
		else:
			i+=1





lien=[]
for a in range(2,101):
	for b in range(2,101):
		lien.append(100000*b*math.log2(a))
'''
i=0
for a in range(2,101):
	for b in range(2,101):
		print(a,b,lien[i],end="")
		i+=1
		input()
	print()
'''

lien.sort()
shit(lien)
print(len(lien))
