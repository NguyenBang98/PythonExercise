def swapPosition(NewList, pos1, pos2):
    NewList[pos1], NewList[pos2] = NewList[pos2], NewList[pos1]
    return NewList
NewList = [23, 65, 19, 90] 
pos1, pos2 = 1, 3
print(swapPosition(NewList, pos1 - 1, pos2 - 1))