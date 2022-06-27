'''
File: sfo_50_find_the_first_non-repeating_character_in_a_string_s1.py
Created Time: 2021-12-09
Author: Krahets (krahets@163.com)
'''

from include import *

# ===== Solution Code =====
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = c not in dic
        return next((c for c in s if dic[c]), ' ')

# ======= Test Case =======
s = "abaccdeff"
# ====== Driver Code ======
slt = Solution()
res = slt.firstUniqChar(s)
print(res)
