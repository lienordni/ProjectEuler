import os

fin=open("./70.txt","r")
fout=open("./70.2.txt","w")
for i in range(1,501):
	s=fin.readline()
	l=s.split(' ')
	fout.write(l[0]+" "+l[1]+"\n")

