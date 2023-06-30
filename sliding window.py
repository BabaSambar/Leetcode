def calculateProfit(array):
    low = array[0]
    high = array[0]
    difference = high-low
    for i in range(len(array)):
        if array[i] < low:
            low = array[i]
            high = array[i]
        elif array[i] > high:
            high = array[i]
        if (high - low) > difference:
            difference = high-low
    return difference

array = [2,4,1]
print(calculateProfit(array))