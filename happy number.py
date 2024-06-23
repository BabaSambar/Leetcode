def isHappy(n: int) -> bool:
    setOfSums = set()
    stringNum = str(n)

    while True:
        # Loop through entire number
        tempsum = 0
        for i in range(len(stringNum)):
            tempsum += (int(stringNum[i]) ** 2)
        print(tempsum)
        # Check if tempsum is one or already in set
        if tempsum == 1:
            return True
        if tempsum in setOfSums:
            return False
        setOfSums.add(tempsum)
        stringNum = str(tempsum)

