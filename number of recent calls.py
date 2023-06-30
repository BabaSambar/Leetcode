class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.queue = []
        print("declared")

    def ping(self, t: int) -> int:
        if len(self.queue) != 0:
            while t-self.queue[0] > 3000:
                self.queue = self.queue[1:]
                if len(self.queue) == 0:
                    break
        self.queue.append(t)
        return len(self.queue)
    
# Only for testing
a = RecentCounter()
l = [642, 1849, 4921, 5936, 5957]
for i in l:
    print(i)
    print(a.ping(i))
