def getConcatenation(nums:list[int]) -> list[int]:
    ans = nums
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans

l = [1,2,1]
print(getConcatenation(l))