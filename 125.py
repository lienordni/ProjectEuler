def cleanse(l): # Gets rid of Redundancies in a sorted array
	m=[l[0]]
	for i in range(1,len(l)):
		if l[i]!=l[i-1]:
			m+=[l[i]]
	return m

l=[5,55,1992991,505,818,42924,77,636,1001,1771,595,1441,34277243,63866836,181,17371,554455,434,1111,148841,313,166661,545,11600611,3242423,485584,6446,21712,95177159,99199,8424248,981189,9313139,363363,3015103,17871,635536,97679,46564,1365631,5479745,4334,63844836,127721,6277726,46433464,19691,108801,444444,65756,6546456,6843486,1077701,139931,44444,9105019,5367635,6106016,81818,525525,904409,52155125,646646,982289,435534,138831,18244281,51015,41214,4776774,3628263,9343439,171171,656656,1949491,161161,188881,4424244,9940499,5718175,137731,923329,1681861,18699681,6844486,11922911,1972791,9435349,4211124,9814189,629926,1224221,191191,45555554,2176712,45755754,68688686,37533573,494494,5276725,17488471,9838389,7355537,5588855,16955961,56722765,972279,5603065,47622674,50244205,944449,52344325,26744762,97299279,53166135,67233276,554455,69933996,52722725,12888821,44366344,5536355,58366385,69388396,16755761,9334339,15822851,9793979,10711701,66999966,964469,92800829,18422481,2904092,4338334,6523256,40211204,53933935,9343439,9072709,5090905,41577514,6831386,13922931,53211235,9563659,6780876,56800865,1690961,72299227,43699634,55344355,62988926,32344323,32611623,16399361,3162613,3187813,69722796,11122111,57488475,5258525,5824285,9051509,49066094,64633646,51488415,95544559]

l.sort()
l=cleanse(l)
print(sum(l))
