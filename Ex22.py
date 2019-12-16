def replaceArr(m, arr):
    for i in range(1, len(arr)):
        arr[i] = (arr[i - 1] + 1) % m
    print(arr)

arr =[5, -1, -1, 1, 2, 3]
replaceArr(7, arr)