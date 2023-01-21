for i in range(int(input())):
    size = int(input())
    array = list(map(int, input().split()))
    if 0 in array:
        c = array.count(0)
        if size == c:
            print(0)
        else:
            print(size - c)
    elif size != len(set(array)):
        print(size)
    else:
        print(size + 1)
