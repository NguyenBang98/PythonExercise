def Fibonacci(x):
    if x <= 0:
        print("Not number")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else: 
        return Fibonacci(x - 1) + Fibonacci(x - 2)
print(Fibonacci(10))