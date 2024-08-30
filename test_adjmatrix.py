from .adjmatrix import AdjMatrix


class TestConstructerNumEdges:

    def test_num_edges3(self):
        a = AdjMatrix(num_edges=3)
        assert a.matrix ==[[1,0,0], [0,1,0], [0,0,1]]

    def test_num_edges2(self):
        a = AdjMatrix(num_edges=2)
        assert a.matrix ==[[1,0], [0,1]]

    def test_num_edges1(self):
        a = AdjMatrix(num_edges=1)
        assert a.matrix ==[[1]]

    def test_num_edges0(self):
        a = AdjMatrix()
        assert a.matrix ==[]

class TestUnion:

    def test_simple(self):
        pass


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
    
class TestTraversals:

    def test_nothing_really_dfs(self):
        edges = SampleData.leet_code_example()
        a = AdjMatrix(edges=edges)
        a.dfs(0)

    def test_nothing_really_bfs(self):
        edges = SampleData.leet_code_example()
        a = AdjMatrix(edges=edges)
        a.bfs(0)  


class TestShortestPath:
    def test_leet_code_example(self):
        edges = SampleData.leet_code_example()
        a = AdjMatrix(edges, 6)
        assert a.shortest_path(0, 5) == [0,1,5]

class TestAllPaths:

    def test_leet_code_example(self):
        edges = SampleData.leet_code_example()
        a = AdjMatrix(edges, 6)
        all_paths = [[0, 1, 5], [0, 1, 4, 5], [0, 2, 4, 5], [0, 3, 4, 5], [0, 2, 4, 1, 5], [0, 3, 4, 1, 5]]
        assert a.all_paths(0, 5) == [[0, 1, 5], [0, 1, 4, 5], [0, 2, 4, 5], [0, 3, 4, 5], [0, 2, 4, 1, 5], [0, 3, 4, 1, 5]]