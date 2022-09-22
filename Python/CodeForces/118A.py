nb = input()
lisx = [""]

for i in nb.lower():
    if (i != "a") and   (i != "e") and (i != "i") and (i != "o") and (i != "u") and(i != "y"):
         lisx.append(".")
         lisx.append(i)


print("".join(lisx))
    
    



