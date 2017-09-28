a=[1]+[0]*100

for n in range(1,100):
    for i in range(n,101):
        a[i]+=a[i-n]

print(a[100])