from common import Node

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = []
        q.append(root)
        while len(q) != 0:
            size = len(q)
            prev = None
            for _ in range(size):
                tmp = q.pop(0)
                if prev is not None:
                    prev.next = tmp
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                prev = tmp
        return root

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    res = Solution().connect(root)

    while res:
        curr = res
        while curr:
            print(curr.val)
            curr = curr.next
        res = res.left
