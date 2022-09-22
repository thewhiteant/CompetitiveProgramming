data = int(input())
ln = [4, 7, 47, 74, 444, 447, 474, 477, 777, 774, 744]

x = False


for i in ln:
	if data % i == 0:
		x = True
		break
	else:
		x = False


if x == True:
	print("YES")
else:
	print("NO")


#done

