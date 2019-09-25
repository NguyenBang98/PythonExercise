def PrimeNumber():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    for i in range(start, end + 1):
        x = 0
        for n in range(1, i + 1):
            if(i % n == 0):
                x += 1
        if(x == 2):
            print(i)


def PrimeNumber2():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    for i in range(start, end + 1):
        if i > 1:
            for n in range(2, i):
                if (i % n == 0):
                    break
            else:
                print(i)
PrimeNumber2()