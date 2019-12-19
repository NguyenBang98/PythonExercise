def swap(NewList):
    size = len(NewList)
    temp = NewList[0]
    NewList[0] = NewList[size - 1]
    NewList[size - 1] = temp
    return NewList
NewList = [12, 35, 9, 56, 24] 
print(swap(NewList))
