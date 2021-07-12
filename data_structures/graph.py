from collections import defaultdict
from queue import Queue


class Graph(defaultdict):

    @property
    def edges(self):
        return [(node, neighbour) for node in self for neighbour in self[node]]

    def bfs(self, start):
        q = Queue()
        visited = []
        print(start)
        q.enqueue(start)
        visited.append(start)
        while q:
            neighbors = self[q.peek()]
            q.dequeue()
            for neighbor in neighbors:
                if neighbor not in visited:
                    print(neighbor, end=' ')
                    visited.append(neighbor)
                    q.enqueue(neighbor)
            print('')


def main():
    g = Graph(list)
    g['a'].append('b')
    g['a'].append('c')
    g['b'].append('d')
    g['b'].append('e')
    g['c'].append('d')
    g['c'].append('e')
    g['a'].append('f')
    g['c'].append('g')
    g['d'].append('g')
    g['h'].append('i')
    g['e'].append('h')
    print(g.edges)
    print(g)
    g.bfs('a')

if __name__ == '__main__':
    main()
