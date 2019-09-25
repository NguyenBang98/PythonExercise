def cubeOfSum(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i ** 3
    return sum

print(cubeOfSum(7))