def twosum(nums, target):
    gap = 0
    for j in range(len(nums)):
        for i in range(len(nums)):
            if i+gap+1 >= len(nums):
                break
            if((nums[i] + nums[i+gap+1]) == target):
                return (i, i+gap+1)
        gap+=1

arr = [3, 2, 3]
print(twosum(arr, 6))

