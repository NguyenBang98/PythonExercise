def factorial():
    n = int(input("Enter the number:"))
    S = 1
    for i in range(1, n + 1):
        S *= i
    print("Factorial of", n, "is", S)
factorial()