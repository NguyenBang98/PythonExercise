def order(x):
    n = 0
    while (x > 0):
        x = x / 10
        n = n + 1
    print(n)
x = 153
order(x)

#def isAmstrong():
#    x = int(input("Enter the number: "))
#    y = x
#    temp = x
#    n = order(x)
#    sum = 0
#    while(temp != 0):
#        r = temp % 10
#        sum = sum + r ** n
#        temp = temp / 10
#   return (sum == y)
#print(isAmstrong())

