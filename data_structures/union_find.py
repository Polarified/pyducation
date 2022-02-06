"""
Create a mapping between element and index. This works with an array.
To find which component a certain element belongs to, we travel up to the root until we find a self loop (an element who's parent is itself).
To unify two elements we find the two root nodes of the groups each element belongs to, then we make one of the root nodes be the parent of the other if they are different.
"""


class UnionFind(list):

    def find(self, n):
        i = self.index(n)
        while self.index(n) != n:
            pass

    def union(self, n, m):
        pass
