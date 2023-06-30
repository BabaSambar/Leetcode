from collections import deque

def asteroidCollision(asteroids):
    stack = deque()
    for i in asteroids:
        while len(stack) > 0 and stack[-1] > 0 and i < 0:
            if i + stack[-1] > 0:
                i = 0
            elif i + stack[-1] < 0:
                stack.pop()
            else:
                i = 0
                stack.pop()
        if i != 0:
            stack.append(i)
    return list(stack)

arr = [2, -6, 4, -9, 1]
print(asteroidCollision(arr))