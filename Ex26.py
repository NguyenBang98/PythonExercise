def removeNthWord(Lst, Word, N):
    newList = []
    count = 0
    for i in Lst:
        if(i == Word):
            count = count + 1
            if(count != N):
                newList.append(i)
        else:
            newList.append(i)
    if(count == 0):
        print("No Item delete")
    else:
        print("New List is: ", newList)
    return newList
Lst = ["geeks", "for", "geeks"] 
Word = "geeks"
N = 2

removeNthWord(Lst, Word, N)
    
          
