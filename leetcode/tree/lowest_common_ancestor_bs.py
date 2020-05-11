from common import TreeNode
from typing import List

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(curr):
            if not curr:
                return False
            left = helper(curr.left)
            right = helper(curr.right)
            mid = curr == p or curr == q
            if mid + left + right >= 2:
                self.ans = curr
            return mid or left or right
        helper(root)
        return self.ans

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    p = root.left
    q = root.left.right.right
    res = Solution().lowestCommonAncestor(root, p, q)
    print(res.val)
