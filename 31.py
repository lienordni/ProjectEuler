def sum_possibilities(target,array): # Needs Nothing
	a=[1]+[0]*target
	for x in array:
		for i in range(x, target+1):
			a[i] += a[i-x]
	return a[target]

print(sum_possibilities(200,[1, 2, 5, 10, 20, 50, 100, 200]))