def uniqueOccurences(arr):
    table = {}
    for i in arr:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    tempList = []
    for i in table.values():
        if i in tempList:
            return False
        else:
            tempList.append(i)
    return True

arr = [1,2]
print(uniqueOccurences(arr))