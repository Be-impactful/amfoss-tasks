for i in range(int(input())):
    key = int(input())
    array = list(map(int, input().split()))
    first = array[key-1]
    second = third = 5
    if first != 0:
        second = array[first-1]
        if second != 0:
            third = array[second-1]
    new_array = [first, second, third]
    new_array.sort()
    array.sort()
    if array == new_array:
        print("YES")
    else:
        print("NO")
