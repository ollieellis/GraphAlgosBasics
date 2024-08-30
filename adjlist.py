from typing import List, Optional

class AdjList:
    """assumes nodes as ints 1 -> n"""
    # __neighbour: List[List[int]] = []

    def __init__(self, edges: Optional[List[List[int]]]=[], num_edges:Optional[int]=0) -> None:
        max_node = 0
        if len(edges) > 0:
            max_node = max(max(l) for l in edges)
        num_edges = max(max_node + 1, num_edges)
        self.__neighbour = [set() for _ in range(num_edges)]
        for l in edges:
            self.union(l[0], l[1])

    def all_paths(self, start_node: int, end_node: int):
        """returns all paths without visiting the same node twice"""
        stack = [[start_node]]
        paths = []
        while stack:
            path = stack.pop(0)
            node = path[-1]
            if node in path[:-1]:
                continue
            if node == end_node:
                paths += [path]
            stack += [path + [i] for i in self.__neighbour[node]]

        return paths

    def shortest_path(self, start_node: int, end_node: int) -> Optional[List[int]]:
        """returns the first found shortest path"""
        stack = [[start_node]]
        visited = set()
        path = []
        while stack:
            path = stack.pop(0)
            node = path[-1]
            if node in visited:
                continue
            if node == end_node:
                return path
            stack += [path + [i] for i in self.__neighbour[node]]
            visited.add(node)

        return None

    def connected(self, start_node: int, end_node: int):
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop(0)
            if node in visited:
                continue
            if node == end_node:
                return True
            stack += self.__neighbour[node]
            visited.add(node)

        return False
    
    def union(self, node1: int, node2: int):
        self.__neighbour[node1].add(node2)
        self.__neighbour[node2].add(node1)

    def dfs(self, start_node, end: Optional[int]=None):
        """just prints the node using dfs travelsal"""
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            stack += self.__neighbour[node]
            visited.add(node)
            print(node)

    def bfs(self, start_node, end: Optional[int]=None):
        """just prints the node using bfs travelsal"""
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop(0)
            if node in visited:
                continue
            stack += self.__neighbour[node]
            visited.add(node)
            print(node)

    @property
    def neighbour(self):
        return self.__neighbour