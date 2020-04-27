class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result

'''
    1
   / \
  2   3
     /
    4 
=> inorder is: 2 - 1 - 4 - 3 
'''
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print("Inorder is: {}".format(Solution().inorderTraversal(root)))