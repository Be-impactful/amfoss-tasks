for i in range(int(input())):
    size = int(input())
    array = list(map(int, input().split()))
    for j in range(2):
        for i in range(size-1):
            if array[size-i-1] - array[size-i-2] >= 0:
                array[size-i-1] -= array[size-i-2]
    array[0] = 0
    ans = 1
    for i in array:
        if i != 0:
            print("NO")
            ans = 0
            break
    if ans:
        print("YES")
