from common import TreeNode

def isValidBST(root: TreeNode) -> bool:
    def solve(node, lower, upper):
        if not node:
            return True
        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False
        if not solve(node.right, node.val, upper):
            return False
        if not solve(node.left, lower, node.val):
            return False
        return True
    return solve(root, None, None)

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    print(isValidBST(root))
