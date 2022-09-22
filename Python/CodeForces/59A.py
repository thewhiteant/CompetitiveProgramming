words = input()
up = 0
low = 0
for word in words:
    if word == word.upper():
            up+=1
    else:
            low += 1         
if  up > low:
    print(words.upper())
else:
    print(words.lower())
