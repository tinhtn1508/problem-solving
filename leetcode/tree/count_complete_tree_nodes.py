from common import TreeNode
from typing import List

class Solution:
    def __init__(self):
        self.count = 0
    def countNodes(self, root: TreeNode) -> int:
        def helper(root):
            if root:
                self.count += 1
            else:
                return
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.count

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(Solution().countNodes(root))
    