x, y = map(int,input().split())
p = list(map(int,input().split()))



total = 0

for i in p:
	if i <= y:
		total += 1
	elif i > y:
		total+= 2
print(total)