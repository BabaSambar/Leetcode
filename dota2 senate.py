def predictPartyVictory(senate):
    senate = list(senate)
    n = len(senate)
    r_queue, d_queue = [], []
    for i in range(len(senate)):
        if senate[i] =="R":
            r_queue.append(i)
        else:
            d_queue.append(i)
    while d_queue and r_queue:
        d = d_queue[0]
        d_queue = d_queue[1:]
        r = r_queue[0]
        r_queue = r_queue[1:]
        if r < d:
            r_queue.append(r + n)
        else:
            d_queue.append(d + n)
    if r_queue:
        return "Radiant"
    else:
        return "Dire"    
    
senate = "RDD"
print(predictPartyVictory(senate))
