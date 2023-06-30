def maxArea(height):
    lp, rp =  0, len(height)-1
    area = 0
    while lp < rp:
        area = max(area, min(height[lp], height[rp]) * (rp - lp))
        if height[lp] <= height[rp]:
            lp += 1
        elif height[lp] > height[rp]:
            rp -= 1
    return area

height = [2,3,4,5,18,17,6]
print(maxArea(height))