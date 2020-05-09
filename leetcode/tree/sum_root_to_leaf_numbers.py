from common import TreeNode
from copy import deepcopy

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        nums = []
        def helper(root, num):
            tmp = deepcopy(num)
            tmp.append(root.val)
            if not root.left and not root.right:
                nums.append(tmp)
                return

            if root.left:
                helper(root.left, tmp)
            if root.right:
                helper(root.right, tmp)
        helper(root, [])
        sum = 0
        for num in nums:
            s = [str(i) for i in num]
            sum += int("".join(s)) 
        return sum            

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(Solution().sumNumbers(root))