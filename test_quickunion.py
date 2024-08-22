from .quickunion import QuickUnion

class TestUnion:

    def test_simple(self):
        qu = QuickUnion(3)
        qu.union(0,2)
        assert qu.parents[0] == qu.parents[2]

    def test_simple_via_connected(self):
        qu = QuickUnion(3)
        qu.union(0,2)
        assert qu.connected(0,2)
        assert not qu.connected(1,2)
        assert not qu.connected(0,1)

    def test_chain_simple_via_connected(self):
        qu = QuickUnion(5)
        [qu.union(*i) for i in [(0,1), (1,2), (2,3), (0,4)]]
        assert qu.connected(0, 3)

class TestNumSets:

    def test_3_disjoint_nodes(self):
        qu = QuickUnion(3)
        assert qu.num_sets() == 3

    def test_4_way_set(self):
        qu = QuickUnion(4)
        qu.union(0,1)
        qu.union(1,2)
        qu.union(0,3)
        assert qu.num_sets() == 1