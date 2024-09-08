#not a graph algo; but something i forgot
from functools import cache

class EditDistance:
    def bottom_up(self, word1: str, word2: str) -> int:
        """bottom up solution to find edit distance from word1 to word2"""
        dp_table = [[0]* (len(word2)+1) for _ in range(len(word1)+1)] #+1 because base is """
        dp_table[0] = [i for i in range(len(word2)+1)]
        for i in range(len(word1)+1):
            dp_table[i][0] = i

        for i in range(1, len(dp_table)):
            for j in range(1, len(dp_table[0])):
                if word1[i-1] == word2[j-1]:
                    dp_table[i][j] = dp_table[i-1][j-1]
                else:
                    edit_distance_ij = 1 + min(dp_table[i-1][j-1], dp_table[i][j-1], dp_table[i-1][j])
                    dp_table[i][j] = edit_distance_ij
        
        return dp_table[-1][-1]

    def top_down(self, word1: str, word2: str) -> int:
        
        @cache
        def rec_get_edit_distance(w1, w2, i1, i2):
            if i1 == 0:
                return i2
            if i2 == 0:
                return i1

            if w1[i1 - 1] == w2[i2 - 1]:
                return rec_get_edit_distance(w1, w2, i1-1, i2-1)

            replace = 1 + rec_get_edit_distance(word1, word2, i1-1, i2-1)
            delete = 1 + rec_get_edit_distance(word1, word2, i1-1, i2)
            add = 1 + rec_get_edit_distance(word1, word2, i1, i2-1)
            return min(replace, delete, add) #+1?

        return rec_get_edit_distance(word1, word2, len(word1), len(word2))

    def print_tbl(self, dp_table, word1, word2):
        header = ["_", " "] + [i for i in word2]
        print(header)
        for i, l in enumerate(dp_table):
            print(["_"] + [word1[i]] + [str(i) for i in l])


