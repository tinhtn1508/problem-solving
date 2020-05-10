from common import TreeNode
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        arr = []
        def helper(root):
            if not root:
                return
            q = [root]
            while len(q) != 0:
                inner = []
                size = len(q)
                for i in range(len(q)):
                    tmp = q.pop(0)
                    if tmp.left:
                        q.append(tmp.left)
                    if tmp.right:
                        q.append(tmp.right)
                    inner.append(tmp.val)
                arr.append(inner[-1])
        helper(root)
        return arr

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().rightSideView(root))