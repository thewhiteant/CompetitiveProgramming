n = input().split()

red = int(n[0])
blue = int(n[1])
lalnil = 0
ekcolor = 0

if red > blue:
    lalnil += blue
    ekcolor = (red - blue) / 2
elif red < blue:
    lalnil += red
    ekcolor = (blue - red) / 2
elif red == blue:
    lalnil = red
print(lalnil,int(ekcolor))