def removeElement(nums: list[int], val:int) -> int:
    if len(nums) == 0:
        return 0
    l=0
    r=len(nums)-1
    while(nums[r] == val):
        r-=1
    while(l<r):
        if nums[l] == val:
            print(r)
            nums[l] = nums[r]
            r-=1
        l+=1
    print(nums)
    return l

l = [3,2,2,3]
print(removeElement(l, 3))