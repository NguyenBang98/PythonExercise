def MonotonicArrDecreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
            break
    return True

def isMonotic(arr):
    return (all (arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all (arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

arr = [6, 5, 4, 4]
print(isMonotic(arr))
