u = int(input())
year = str(u+1)



while True:
    if year[0] == year[1] or year[1] == year[2] or year[2] == year[3] or year[0] == year[3] or year[0]==year[2] or year[1] == year[3]:
        year = str(int(year) + 1)
    else:
        print(year)
        break