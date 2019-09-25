def isPrimeNumber(x):
    for i in range(2, x//2):
        if (x % i == 0):
            print(x, "is not prime number")
            break
    else:
        print(x, "is prime number")             
isPrimeNumber(6)