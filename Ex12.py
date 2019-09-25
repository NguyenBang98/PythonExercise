def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * i

        i += 1
    return


k = 4
n = 5
print("Position of n'th multiple of k inFibonacci Series is", findPosition(k, n))