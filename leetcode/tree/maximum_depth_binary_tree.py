class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    def solve(root, d):
        if not root:
            return d
        d += 1
        return max(solve(root.left, d), solve(root.right, d))
    return solve(root, 0)

if __name__ == "__main__":
    root = TreeNode(3)
    # root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth(root))