def removeStars(s):
    stack = []
    res = ""
    for i in s:
        if i != "*":
            stack.append(i)
        else:
            stack.pop()
    for i in stack:
        res = res + i
    return res

s = "erase****"
print(removeStars(s))