'''
File: sfo_55-ii_balanced_binary_tree_s2.py
Created Time: 2021-12-09
Author: Krahets (krahets@163.com)
'''

from include import *

# ===== Solution Code =====
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return (
            abs(self.depth(root.left) - self.depth(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
            if root
            else True
        )

    def depth(self, root):
        return max(self.depth(root.left), self.depth(root.right)) + 1 if root else 0

# ======= Test Case =======
root = list_to_tree([3, 9, 20, None, None, 15, 7, None, None, None, None])
# ====== Driver Code ======
slt = Solution()
res = slt.isBalanced(root)
print(res)
