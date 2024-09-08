#not a graph algo; but something i forgot

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
    
    def print_tbl(self, dp_table, word1, word2):
        header = ["_", " "] + [i for i in word2]
        print(header)
        w1 = " "+word1
        for i, l in enumerate(dp_table):
            print([w1[i]] + [str(i) for i in l])



