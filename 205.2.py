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

for i in range(1,37):
	print(i,n[i])
