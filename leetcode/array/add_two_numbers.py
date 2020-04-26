"""
Problem:
    - You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    - You may assume the two numbers do not contain any leading zerom expect the number 0 itself.
Example:
    - Input:(2 -> 4 -> 3) + (5 -> 6 -> 4)
    - Output: 7 -> 0 -> 8
    - Explanation: 342 + 465 = 807
Solution:
    - Traverse both lists and keep track of sum and carry for each digit
Cost:
    - Time: O(max(m, n)) 
    - Space: O(max(m, n))
    - m and n are lengths of two lists 
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumber(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while p1 is not None or p2 is not None:
            x = p1.val if p1 is not None else 0
            y = p2.val if p2 is not None else 0
            s = x + y + carry
            carry = int(s / 10)
            curr.next = ListNode(int(s % 10))
            curr = curr.next
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
        curr.next = ListNode(carry) if carry > 0 else None
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = Solution().addTwoNumber(l1, l2);
    while result is not None:
        print(result.val)
        result = result.next
