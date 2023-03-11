# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time complexty : log
#dfs?
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.value_list = []
        self.return_value = True
        self.dfs(root)
        print(self.value_list)
        return self.return_value
        

    def dfs(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if root is None:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            print(root.val, largerThan, lessThan)
            self.return_value = False
            return False        

      
        self.value_list.append(root.val)
        self.dfs(root.left, min(lessThan, root.val), largerThan)
        self.dfs(root.right, lessThan, max(largerThan, root.val))    
        return self.return_value
        
        
        
        
        