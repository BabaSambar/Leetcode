def decodeString(s):
    stack = []
    for i in s:
        if i != "]":
            stack.append(i)
        else:
            k = ""
            substr = ""
            while stack[-1] != "[" and stack:
                substr = stack.pop() + substr
            stack.pop()
            while stack and stack[-1].isdigit():
                k = stack[-1] + k
                stack.pop()
            stack.append(int(k) * substr)
    return "".join(stack)
s = "2[abc]3[cd]ef"
print(decodeString(s))