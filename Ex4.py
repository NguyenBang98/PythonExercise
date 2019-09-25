def CompoundInterest():
    P = int(input("Enter the principle amount: "))
    T = int(input("Enter the time: "))
    R = float(input("Enter the rate: "))
    return P * ((1 + R / 100) ** T)
print(CompoundInterest())