for i in range(int(input())):
    size = int(input())
    array = list(map(int, input().split()))
    start = 0
    end = size-1
    for j in range(size-1):
        if array[j] > 0:
            start = j
            break
    new_array = array[start:end]
    zero_count = new_array.count(0)
    if zero_count == end:
        print(0)
    else:
        print(sum(new_array) + zero_count)
