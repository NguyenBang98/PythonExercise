def splitArr(arr, k, n):
    for i in range(0, n):
        x = arr[0]
        for j in range(0, k - 1):
            arr[j] = arr[j + 1]
        arr[k - 1] = x

arr = [12, 10, 5, 6, 52, 36] 
n = len(arr) 
position = 2
  
splitArr(arr, n, position) 
  
for i in range(0, n):  
    print(arr[i], end = ' ') 
