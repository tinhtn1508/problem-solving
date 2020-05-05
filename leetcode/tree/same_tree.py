from common import TreeNode
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

if __name__ == "__main__":
    q = TreeNode(3)
    q.left = TreeNode(4)
    q.left = TreeNode(5)
    p = TreeNode(3)
    p.left = TreeNode(4)
    p.left = TreeNode(5)
    if Solution().isSameTree(q, p):
        print("Same")
    else:
        print("Not Same")