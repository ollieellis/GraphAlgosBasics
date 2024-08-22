from copy import deepcopy
from .disjointset import DisjointSet

class QuickUnion(DisjointSet):

    def __init__(self, n):
        self.__parents = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        root_p = self.root(p)
        root_q = self.root(q)
        if root_p != root_q:
            self.__parents[q] = root_p


    def connected(self, p: int, q: int) -> bool:
        return self.root(q) == self.root(p)

    def root(self, p: int):
        while self.__parents[p] != p:
            p = self.__parents[p]
        return p
    
    def num_sets(self):
        roots = [self.root(i) for i in self.__parents]
        return len(set(roots))

    @property
    def parents(self):
        return deepcopy(self.__parents)