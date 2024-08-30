from typing import List, Optional

class AdjMatrix:
    """assumes nodes as ints 1 -> n"""
    __matrix = List[List[int]]

    def __init__(self, edges: Optional[List[List[int]]]=[], num_edges:Optional[int]=0) -> None:
        max_node = 0
        if len(edges) > 0:
            max_node = max(max(l) for l in edges)
        num_edges = max(max_node+1, num_edges)
        self.__matrix = [[0]*num_edges for _ in range(num_edges)]
        for i in range(num_edges):
            self.__matrix[i][i] = 1

        for i in edges:
            self.union(i[0], i[1])

    def all_paths(self, __from: int, __to: int, bfs: bool=True):
        stack = [[__from]]
        paths = []
        while stack:
            path =  stack.pop(0)
            node = path[-1]
            if node in path[:-1]:
                continue
            if node == __to:
                paths += [path]
            stack += [path + [n] for n in self.get_adjacents(node)]
        
        return paths


    def shortest_path(self, __from: int, __to: int):
        stack = [[__from]]
        visited = set()
        while stack:
            path = stack.pop(0)
            node = path[-1]
            if node in visited:
                continue
            if node == __to:
                return path
            stack += [path + [n] for n in self.get_adjacents(node)]
            visited.add(node)

        return None


    def connected(self, __from: int, __to: int):
        return self.__matrix[__from][__to]
    
    def union(self, __node1: int, __node2: int):
        self.__matrix[__node1][__node2] = 1
        self.__matrix[__node2][__node1] = 1


    def dfs(self, start_node, end: Optional[int]=None):
        """just prints the node using dfs travelsal"""
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            print(node)
            if end is not None:
                if node == end:
                    return
            stack += self.get_adjacents(node)

    def bfs(self, start_node, end: Optional[int]=None):
        """just prints the node using bfs travelsal"""
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop(0)
            if node in visited:
                continue
            visited.add(node)
            print(node)
            if end is not None:
                if node == end:
                    return
            stack += self.get_adjacents(node)

    def get_adjacents(self, node):
        return [i for i, con in enumerate(self.__matrix[node]) if con ==1 and i != node]

    @property
    def matrix(self):
        return self.__matrix