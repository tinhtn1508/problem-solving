from common import TreeNode
from copy import deepcopy

class Solution():
    def __init__(self):
        self.out = []
    def pathSum(self, root: TreeNode, sum: int):
        def solve(root, sum, path):
            if not root:
                return
            tmp = deepcopy(path)
            tmp.append(root.val)
            if sum == root.val and not root.left and not root.right:
                self.out.append(tmp)
                return
            solve(root.left, sum - root.val, tmp)
            solve(root.right, sum - root.val, tmp)
        path = []
        solve(root, sum, path)
        return self.out

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

    print(Solution().pathSum(root, 22))
    print(Solution().pathSum(root, 27))
