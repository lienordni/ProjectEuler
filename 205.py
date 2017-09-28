a=[0]*9
n=[0]*37
for a[0] in range(1,5):
	for a[1] in range(1,5):
		for a[2] in range(1,5):
			for a[3] in range(1,5):
				for a[4] in range(1,5):
					for a[5] in range(1,5):
						for a[6] in range(1,5):
							for a[7] in range(1,5):
								for a[8] in range(1,5):
									n[sum(a)]+=1

b=[0]*6
m=[0]*37

for b[0] in range(1,7):
	for b[1] in range(1,7):
		for b[2] in range(1,7):
			for b[3] in range(1,7):
				for b[4] in range(1,7):
					for b[5] in range(1,7):
						m[sum(b)]+=1

s=0
for i in range(1,37):
	print(i,"    ",n[i],"     ",m[i],"    ",sum(m[:i]),"    ",n[i]*sum(m[:i]))
	s+=n[i]*sum(m[:i])
print(s,s/((2**24)*(3**6)))