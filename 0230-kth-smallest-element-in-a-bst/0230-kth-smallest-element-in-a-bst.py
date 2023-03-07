# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        def indoor(root):
        
            if root is None:
                return []
            left = indoor(root.left)
            right = indoor(root.right)
            return left + [root.val] + right
        ans = indoor(root)
  
        return ans[k-1]
        
        