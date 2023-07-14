def pivotIndex(nums):
    preSum, sufSum = [],[]
    temp = 0
    for i in nums:
        temp = temp + i
        preSum.append(temp)
    temp = 0
    for i in range(len(nums)-1, -1, -1):
        temp = temp + nums[i]
        sufSum.insert(0,temp)
    for i in range(len(nums)):
        if preSum[i] == sufSum[i]:
            return i

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))