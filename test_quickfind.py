from .quickfind import QuickFind

class TestUnion:

    def test_simple_union(self):
        qf = QuickFind(3)
        qf.union(0, 2)
        assert qf.roots == [0,1,0]

    def test_3_way_simple_union(self):
        qf = QuickFind(3)
        qf.union(0, 1)
        qf.union(1, 2)
        assert len(set(qf.roots)) == 1

    def test_3_way_simple_other(self):
        qf = QuickFind(3)
        qf.union(0, 1)
        qf.union(0, 2)
        assert len(set(qf.roots)) == 1

    def test_children_follow(self):
        qf = QuickFind(4)
        qf.union(0, 1)
        qf.union(2, 3)
        assert len(set(qf.roots)) == 2
        qf.union(0, 3)
        assert len(set(qf.roots)) == 1

class TestConnected:

    def test_simple_conn(self):
        qf = QuickFind(3)
        qf.union(0, 2)
        assert qf.connected(0, 2)
    
    def test_simple_conn_negative(self):
        qf = QuickFind(3)
        qf.union(0, 2)
        assert not qf.connected(1, 2)

    def test_children_follow(self):
        qf = QuickFind(4)
        qf.union(0, 1)
        qf.union(2, 3)
        assert not qf.connected(0, 3)
        qf.union(0, 2)
        assert qf.connected(0, 2)

class TestNumSets:

    def test_all_distinct(self):
        qf = QuickFind(4)
        assert qf.num_sets() == 4

    def test_children_follow(self):
        qf = QuickFind(4)
        qf.union(0, 1)
        qf.union(2, 3)
        assert qf.num_sets() == 2
        qf.union(0, 2)
        assert qf.num_sets() == 1