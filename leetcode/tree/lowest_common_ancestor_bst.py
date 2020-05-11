from common import TreeNode
from typing import List

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val, p_val, q_val = root.val, p.val, q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(0)
    root.left.left.right = TreeNode(4)
    root.left.left.right.left = TreeNode(3)
    root.left.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = TreeNode(2)
    q = TreeNode(4)
    res = Solution().lowestCommonAncestor(root, p, q)
    print(res.val)