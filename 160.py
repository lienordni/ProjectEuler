import math

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def self(i):
	return (math.factorial(i)//10**(exponent(i,5)))%10**5


print(self(2500))
print(self(62500))
print(self(312500))