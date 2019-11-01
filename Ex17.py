def largest_Arr(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

arr = [1, 5, 10, 20, 3]
print(largest_Arr(arr))
