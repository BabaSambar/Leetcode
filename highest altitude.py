def largestAltitude(gain) -> int:
    altitudes = [0]
    highest = 0
    for i in gain:
        altitudes.append(altitudes[-1]+i)
        highest = max(highest, altitudes[-1])
        print(altitudes)
    return highest

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))