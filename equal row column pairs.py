def equalPairs(grid) -> int:
    rowHashMap = dict()

    for i in range(len(grid)):
        if tuple(grid[i]) not in rowHashMap:
            rowHashMap.update({tuple(grid[i]) : 1})
        else:
            rowHashMap.update({tuple(grid[i]) : rowHashMap[tuple(grid[i])] + 1})

    l = []
    flipped_grid = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            l.append(grid[j][i])
        flipped_grid.append(l)
        l = []

    count = 0
    for i in range(len(flipped_grid)):
        if tuple(flipped_grid[i]) not in rowHashMap:
            rowHashMap.update({tuple(flipped_grid[i]) : 0})
        else:
            count += rowHashMap[tuple(flipped_grid[i])]
    return count

grid = [[13,13],[13,13]]
print(equalPairs(grid))
