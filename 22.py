def score(name):
	s=0
	for i in range(0,len(name)):
		s+=ord(name[i])-64
	return s

lien=open("22.txt")
names=(lien.read()).split("\",\"")

sort=sorted(names)
i=0
q=0
while i<=5162:
	q+=(i+1)*score(sort[i])
	i+=1
print(q)