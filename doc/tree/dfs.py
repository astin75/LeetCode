def dfs(cur_node):
    if root is None:
        return 
    dfs(cur_node.left)
    dfs(cur_node.right)
    
dfs(root)