from common import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        self.helper(root)        

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.arr.append(root.val)
        self.helper(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.pop(0)        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.arr) != 0

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    bst = BSTIterator(root)
    for _ in range(5):
        print(bst.next())
        print(bst.hasNext())