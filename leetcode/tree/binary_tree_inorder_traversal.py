from common import TreeNode

def inorderTraversal(root: TreeNode) -> list:
    result = []
    def solve(root: TreeNode):
        if not root:
            return
        solve(root.left)
        result.append(root.val)
        solve(root.right)
        return result
    return solve(root)

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
    print("Inorder is: {}".format(inorderTraversal(root)))