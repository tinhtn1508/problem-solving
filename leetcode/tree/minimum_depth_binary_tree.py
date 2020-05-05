from common import TreeNode

class Solution():
    def __init__(self):
        self.out = 999999999
    def minDepth(self, root: TreeNode) -> int:
        def solve(root: TreeNode, l):
            if not root:
                return
            if not root.left and not root.right:
                self.out = min(self.out, l)
                return
            solve(root.left, l + 1)
            solve(root.right, l + 1)
        if not root:
            return 0
        solve(root, 1)
        return self.out
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().minDepth(root))