from abc import ABC, abstractmethod

class DisjointSet(ABC):

    """Abstract class that disjoint set implementations implement; ie quick find/union ect"""

    @abstractmethod
    def union(self, p: int, q: int) -> None:
        """Joins node p and q"""
        pass

    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        """ Returns if node p and q are connected"""
        pass

    @abstractmethod
    def num_sets(self):
        pass

    @abstractmethod
    def root(self, p: int):
        """ Returns Root of node P"""
        pass