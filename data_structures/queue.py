class Queue(list):

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        self.pop(0)

    def peek(self):
        return self[0]

def main():
    q = Queue()
    print(q)
    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(4)
    print(q)


if __name__ == '__main__':
    main()
