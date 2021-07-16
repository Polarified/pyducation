from collections import defaultdict

class BinaryHeap(list):
    def __init__(self, comparator):
        super(list, self).__init__()
        self._comparator = comparator
        self._hashtable = defaultdict(list)

    def insert(self, n):
        i = len(self)
        self.append(n)
        self._hashtable[n].append(i)
        if i == 0:
            return
        pi = (i - 2) // 2 if i % 2 == 0 else (i - 1) // 2

        while self._comparator(self[i], self[pi]) == self[i]:
            self[i], self[pi] = self[pi], self[i]
            i = pi
            pi = (i - 2) // 2 if i % 2 == 0 else (i - 1) // 2

    def poll(self):
        self[0], self[-1] = self[-1], self[0]
        self.pop()
        i = 0
        # write logic for bubbling down, don't care for it
        pass

    def remove(self, n):
        # first linear search for the value, then do the same as polling
        # this sucks, so we can use a hashtable to improve to logn.
        pass

    def __str__(self):
        x = 1
        y = x
        r = ''
        for i in self:
            r += (str(i) + ' ')
            y -= 1
            if y == 0:
                x *= 2
                y = x
                r += '\n'
        return r


bh = BinaryHeap(min)
bh.append(1)
bh.append(2)
bh.append(3)
bh.append(4)
bh.append(5)
bh.append(6)
print(bh)
