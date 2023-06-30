def sqrt(number):
    temp = number
    while temp*temp > number:
        temp = int((temp + (number/temp)) / 2)
        print(temp)
    return temp

def sqrt2(number):
    temp = number
    while temp*temp > number:
        temp = int((temp + (number/temp)) / 2)
        print(temp)
    return temp

print(sqrt(180))
print("~~~~~")
print(sqrt2(180))