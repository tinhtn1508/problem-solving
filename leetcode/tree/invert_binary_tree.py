from common import TreeNode
from typing import List

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return
            
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)
        helper(root)
        return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root = Solution().invertTree(root)
    print(root.val, root.left.val, root.right.val)