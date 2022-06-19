'''
Height of a Binary Tree

'''

def height(root):
    if root.left == None and root.right == None:
        return 0
    if root.left == None:
        return height(root.right)+1
    if root.right == None:
        return height(root.left)+1
    return max(height(root.left)+1, height(root.right)+1)
