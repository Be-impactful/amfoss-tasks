n = input()
l = len(n)
k = y = 0
a = 1
if l == 1:
    print(0)
else:
    for i in range(l):
        k += int(n[i])

    if k > 9:
        a += 1
        s = str(k)
        z = len(s)
        for j in range(z):
            y += int(s[j])
    else:
        a += 0

    if y > 9:
        a += 1
        s = str(y)
        z = len(s)
        for j in range(z):
            y += int(s[j])
    else:
        a += 0
    print(a)
