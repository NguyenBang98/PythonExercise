import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x
def isFibonacci(x):
    return isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4)
for x in range(1, 11):
    if(isFibonacci(x)):
        print(x, "is Fibonacci number")
    else:
        print(x, "is not Fibonacci number")