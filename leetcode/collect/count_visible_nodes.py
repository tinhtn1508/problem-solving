import sys
sys.path.append('../tree')
from common import TreeNode

def solution(root):
    def util(root, maxSoFar):
        if not root:
            return 0
        count = 0
        if root.val >= maxSoFar:
            count = 1
            maxSoFar = root.val
        return count + util(root.left, maxSoFar) + util(root.right, maxSoFar)
    return util(root, -999)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(21)
    root.right.left = TreeNode(1)
    print(solution(root))