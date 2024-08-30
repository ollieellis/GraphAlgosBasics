from .adjlist import AdjList

class SampleData:

    @staticmethod
    def leet_code_example():
        return [
            [0, 1],
            [0, 3],
            [0, 2],
            [1, 4],
            [1, 5],
            [4, 5],
            [4, 2],
            [4, 3],
        ]
    
class TestConstructerNumEdges:

    def test_num_edges3(self):
        a = AdjList(num_edges=3)
        assert a.neighbour == [set(), set(), set()]

    def test_num_edges2(self):
        a = AdjList(num_edges=2)
        assert a.neighbour == [set(), set()]

    def test_num_edges1(self):
        a = AdjList(num_edges=1)
        assert a.neighbour ==[set()]

    def test_num_edges0(self):
        a = AdjList()
        assert a.neighbour ==[]

class TestUnion:

    def test_simple(self):
        a = AdjList(num_edges=3)
        a.union(0, 2)
        assert a.neighbour == [set([2]), set(), set([0])]

class TestTraversals:

    def test_nothing_really_dfs(self):
        edges = self.get_edges()
        a = AdjList(edges=edges)
        a.dfs(0)

    def test_nothing_really_bfs(self):
        edges = self.get_edges()
        a = AdjList(edges=edges)
        a.bfs(0)  

    def get_edges(self):
        return [
            [0, 1],
            [0, 3],
            [0, 2],
            [1, 4],
            [1, 5],
            [4, 5],
            [4, 2],
            [4, 3],
        ]
    
class TestConnected:
    def test_simple(self):
        edges = SampleData.leet_code_example()
        a = AdjList(edges, 7)
        assert not a.connected(0, 6)
    
    def test_simple_connected(self):
        edges = SampleData.leet_code_example()
        a = AdjList(edges, 7)
        assert a.connected(0, 5)


class TestShortestPath:
    def test_leet_code_example(self):
        edges = SampleData.leet_code_example()
        a = AdjList(edges, 6)
        assert a.shortest_path(0, 5) == [0,1,5]

class TestAllPaths:

    def test_leet_code_example(self):
        edges = SampleData.leet_code_example()
        a = AdjList(edges, 6)
        all_paths = [[0, 1, 5], [0, 1, 4, 5], [0, 2, 4, 5], [0, 3, 4, 5], [0, 2, 4, 1, 5], [0, 3, 4, 1, 5]]
        assert a.all_paths(0, 5) == [[0, 1, 5], [0, 1, 4, 5], [0, 2, 4, 5], [0, 3, 4, 5], [0, 2, 4, 1, 5], [0, 3, 4, 1, 5]]