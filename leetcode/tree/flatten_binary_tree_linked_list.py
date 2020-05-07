from common import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp = []
        def solve(root):
            if not root:
                return
            tmp.append(root.val)
            solve(root.left)
            solve(root.right)
        
        solve(root)
        if tmp:
            tmp.pop(0)
            while tmp:
                if root:
                    root.left = None
                    root.right = TreeNode(tmp.pop(0))
                    root = root.right

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten(root)
    
    while root:
        print(root.val)
        root = root.right
