class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.parent = TreeNode(-float('inf'))
        self.first = True

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root, arr):
            if not root:
                return
            solve(root.left, arr)
            if root.val <= self.parent.val:
                if self.first:
                    arr[0] = self.parent
                    self.first = False
                arr[1] = root
            self.parent = root
            solve(root.right, arr)
        arr = [None, None]
        solve(root, arr)
        arr[0].val, arr[1].val = arr[1].val, arr[0].val

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    Solution().recoverTree(root)
    print("root: {}".format(root.val))
    print("root.left: {}".format(root.left.val))
    print("root.left.right: {}".format(root.left.right.val))
