def beautySum(s: str) -> int:
    substrings = {}
    counter = len(s)
    while counter > 2:
        x, y = 0, counter
        for i in range((len(s)+1)-counter):
            substr = s[x:y]
            # print(substr)
            if calculateBeauty(substr) > 0:
                substrings[substr] = calculateBeauty(substr)
            x, y = x+1, y+1
        counter -= 1
    return sum(substrings.values())

def calculateBeauty(s: str) -> int:
    dictionary = {}
    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    diff = max(dictionary.values()) - min(dictionary.values())
    return diff

s = "aabcbaa"
print(beautySum(s))