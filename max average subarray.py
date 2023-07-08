def findMaxAverage(nums, k):
    sum = 0
    counter = 0
    for i in range(k):
        sum += nums[i]
    average = sum/k
    for i in range(k, len(nums)):
        sum += nums[i]
        sum -= nums[counter]
        counter += 1
        average = max(average, (sum/k))
    return average
arr = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(arr, k))