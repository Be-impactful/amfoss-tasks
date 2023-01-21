groups = int(input())
sum = sum(list(map(int, input().split())))
if sum % 4 == 0:
    print(sum//4)
else:
    print(sum//4 + 1)
