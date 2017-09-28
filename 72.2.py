def totient_array(n): # Needs nothing
	phi=[0]+[1]+[i for i in range(2,n+1)]
	
	for i in range(2,n+1):
		if phi[i]==i:
			j=i
			while j<=n:
				phi[j]=(phi[j]//i)*(i-1)
				j+=i
	return phi

def totient_sum(n): # Needs totient_array()
	return sum(totient_array(n))

print(totient_sum(12000))