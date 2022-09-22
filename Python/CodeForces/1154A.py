ao = list(map(int, input().split()))
p = max(ao)

if p == ao[0]:
    a = p - ao[1]
    b = p - ao[2]
    c = p - ao[3]
elif p == ao[1]:
    a = p - ao[0]
    b = p - ao[2]
    c = p - ao[3]
elif p == ao[2]:
    a = p - ao[0]
    b = p - ao[1]
    c = p - ao[3]
elif p == ao[3]:
    a = p - ao[0]
    b = p - ao[1]
    c = p - ao[2]

print(c,b,a)



