def findDifference(nums1, nums2): 
    hash1, hash2, ans1, ans2 = set([]), set([]), set([]), set([])
    for i in nums1:
        hash1.add(i)
    for i in nums2:
        if i not in hash1:
            hash2.add(i)
            ans2.add(i)
    for i in hash1:
        if i not in nums2:
            ans1.add(i)
    return [list(ans1), list(ans2)]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))

# nums1 =
# [-80,-15,-81,-28,-61,63,14,-45,-35,-10]
# nums2 =
# [-1,-40,-44,41,10,-43,69,10,2]
# Output
# [[-61,-28,14,-81,-80,-15,-45,-10,-35,63],[-1,-40,-44,41,10,-43,69,10,2]]
# Expected
# [[-81,-35,-10,-28,-61,-45,-15,14,-80,63],[-1,2,69,-40,41,10,-43,-44]]