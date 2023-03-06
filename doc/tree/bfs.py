from collections import deque

class Node:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None
        
def bfs(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.val)
        
        if cur_node.left:
            q.append(cur_node.left)
        elif cur_node.right:
            q.append(cur_node.right)
    return visited
root = []
bfs()