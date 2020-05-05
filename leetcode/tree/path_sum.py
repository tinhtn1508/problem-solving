from common import TreeNode

def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if sum == root.val and not root.left and not root.right:
        return True
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print(hasPathSum(root, 22))
    print(hasPathSum(root, 27))
