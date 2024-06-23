def isValid(s:str) -> bool:
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            temp = ""
            if i == ")":
                temp = "("
            elif i == "]":
                temp = "["
            elif i == "}":
                temp = "{"
            if temp != stack[-1]:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False


print(isValid("([]())"))