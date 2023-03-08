# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        visted = []
        q = deque([root])
        step = 0
        
        while q:
            level_q = []
            cur_node = q.popleft()
            if isinstance(cur_node, list):
                temp_list = []
                
                for i in cur_node:
                    
                    temp_list.append(i.val)
                      
                    if i.left:
                        level_q.append(i.left)
                    if i.right:
                        level_q.append(i.right)
                if level_q:
                    q.append(level_q)
                visted.append(temp_list)
            else:
                visted.append([cur_node.val])
                if cur_node.left:
                    level_q.append(cur_node.left)
                if cur_node.right:
                    level_q.append(cur_node.right)
                if level_q:
                    q.append(level_q)                

            step+=1
        print(visted)
        return visted
            