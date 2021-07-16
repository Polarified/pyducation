class Queue(list):

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        self.pop(0)

    def peek(self):
        return self[0]

class PriorityQueue(Queue):
    def __init__(self, comparator):
        super(PriorityQueue, self).__init__()
        self._comparator = comparator

    def dequeue(self):
        self.remove(self._comparator(self))

def main():
    q = Queue()
    pq = PriorityQueue(min)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(0)

    pq.enqueue(1)
    pq.enqueue(3)
    pq.enqueue(2)
    pq.enqueue(0)
    print(q, pq)

    q.dequeue()
    pq.dequeue()
    print(q, pq)

if __name__ == '__main__':
    main()
