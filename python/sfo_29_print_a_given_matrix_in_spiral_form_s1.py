'''
File: sfo_29_print_a_given_matrix_in_spiral_form_s1.py
Created Time: 2021-12-09
Author: Krahets (krahets@163.com)
'''

from include import *

# ===== Solution Code =====
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            res.extend(matrix[t][i] for i in range(l, r + 1))
            t += 1
            if t > b: break
            res.extend(matrix[i][r] for i in range(t, b + 1))
            r -= 1
            if l > r: break
            res.extend(matrix[b][i] for i in range(r, l - 1, -1))
            b -= 1
            if t > b: break
            res.extend(matrix[i][l] for i in range(b, t - 1, -1))
            l += 1
            if l > r: break
        return res

# ======= Test Case =======
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# ====== Driver Code ======
slt = Solution()
res = slt.spiralOrder(matrix)
print(res)
