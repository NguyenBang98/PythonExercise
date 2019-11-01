def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr, n)

def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

def printArr(arr, size):
    for i in range(size):
        print("%d"% arr[i], end=" ")

def leftRotate1(arr, d, n):
    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)





arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArr(arr, 7) 