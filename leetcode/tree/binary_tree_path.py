from typing import List
from common import TreeNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        res = []
        def helper(root, out):
            if not root.left and not root.right:
                res.append(out + str(root.val))
                return
            out += str(root.val) + "->"
            if root.left:
                helper(root.left, out)
            if root.right:
                helper(root.right, out)
        helper(root, "")
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().binaryTreePaths(root))