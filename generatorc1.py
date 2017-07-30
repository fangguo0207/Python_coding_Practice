def triangle(gra):
	Y=[1]
	yield Y
	Y=[1,1]
	n=1
	while n < gra:
		yield Y
		Y=[1]+[Y[i]+Y[i+1] for i in range(n)]+[1]
		n=n+1
	return "try"

for t in triangle(10):
	print(t)