def product(array):
    result = [1]
    num = 1
    for i in range(len(array)-1):
        num *= array[i]
        result.append(num)
    num = 1
    for i in range(len(array)-1, 0, -1):
        num *= array[i]
        result[i-1] *= num
    return result

array = [1,2]
print(product(array))