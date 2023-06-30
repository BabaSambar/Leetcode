def increasingTriplet(nums):
    minList, maxList = [0]*(len(nums)), [0]*(len(nums))
    # Calculate minList
    minList[0] = nums[0]
    for i in range(1, len(nums)):
        minList[i] = min(minList[i-1], nums[i])    
    # Calculate maxList
    maxList[-1] = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        maxList[i] = max(nums[i], maxList[i+1])
    # Check for triplet
    for i in range(len(nums)):
        if minList[i] < nums[i] and maxList[i] > nums[i]:
            print((minList[i], nums[i], maxList[i]))
            return True
    return False

nums = [6,7,1,2]
print(increasingTriplet(nums))
