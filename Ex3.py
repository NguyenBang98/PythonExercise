def SimpleInterest():
    P = int(input("Enter the principle amount: "))
    R = float(input("Enter the rate: "))
    T = int(input("Enter the time: "))
    return P * T * R / 100

print(int(SimpleInterest()))