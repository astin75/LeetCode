class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_dict = {}
        r_dict = {}
        rc_dict = {}   
        for gi in range(3):
            for gj in range(3):
                for i1 in range(3):
                    for j1 in range(3):
                        ii = gi * 3
                        jj = gj * 3
                        i = i1 + jj
                        j = j1 + ii

                        a = board[i][j]

                        if a != "." and rc_dict.get(a):
                            return False
                        elif a != ".":
                            rc_dict[a] = True

                        if r_dict.get(i):
                            pass
                        else:
                            r_dict[i] = {}

                        if a != "." and r_dict[i].get(a):
                            return False
                        elif a != ".":
                            r_dict[i][a] = True

                        if c_dict.get(j):
                            pass
                        else:
                            c_dict[j] = {}

                        if a != "." and c_dict[j].get(a):
                            return False
                        elif a != ".":
                            c_dict[j][a] = True
                rc_dict = {}
        return True

