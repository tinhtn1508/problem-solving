from common import TreeNode

class Solution():
    def __init__(self):
        self.maxs = -9999999999
    
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root: TreeNode) -> int:
            ls = 0
            rs = 0
            if not root.left and not root.right:
                self.maxs = max(self.maxs, root.val)
                return root.val
            if root.left:
                ls = helper(root.left)
            if root.right:
                rs = helper(root.right)
            
            if ls >= 0 and rs >= 0:
                self.maxs = max(self.maxs, root.val + ls + rs)
                return root.val + max(ls, rs)
            elif ls < 0 and rs >= 0:
                self.maxs = max(self.maxs, root.val + rs)
                return root.val + rs
            elif ls >= 0 and rs < 0:
                self.maxs = max(self.maxs, root.val + ls)
                return root.val + ls
            else:
                self.maxs = max(self.maxs, root.val)
                return root.val
        helper(root)
        return self.maxs

if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))
