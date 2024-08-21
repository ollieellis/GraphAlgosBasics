from copy import deepcopy
from .disjointset import DisjointSet
        
class QuickFind(DisjointSet):

    """
        Assumes nodes ranging from 0->n; (As __roots are stored; no deletion possible)
    """

    def __init__(self, n: int) -> None:
        self.__roots = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        root_p = self.root(p)
        root_q = self.root(q)
        if root_p == root_q:
            return 
       
        for i, root in enumerate(self.__roots):
            if root == root_q:
                self.__roots[i] = root_p
    
    def connected(self, p: int, q: int) -> bool:
        return self.__roots[p] == self.__roots[q]
    
    def num_sets(self):
        return len(set(self.__roots))
    
    def root(self, p: int):
        return self.__roots[p]
    
    @property
    def roots(self):
        """returns a copy of self.__roots"""
        return deepcopy(self.__roots)