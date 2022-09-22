datax = input()
data = datax[1:-1].replace(",","")
data = data.split()
data.sort()
count = 0
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count+=1

if count > 0:
        print(count+1)
elif len(set(data)) == 1:
       print(1)
else:
      print(count)
