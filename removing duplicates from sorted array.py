def removeDuplicates(nums: list[int]) -> int:
    l, r = 0, 1
    while(r < len(nums)):
        if nums[l] < nums[r]:
            nums[l+1] = nums[r]
            l+=1
        r+=1
    return l+1, nums


l = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(l))
