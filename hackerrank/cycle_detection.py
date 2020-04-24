'''
 Problem:
  - A linked list is said to contain a cycle if any node is visited more than once while traversing the list
 Solution:
  - Use two pointer to traverse, one is 1 step and another is 2 steps
 Cost:
 - O(n): n is length of linked list
'''
class SinglyLinkedListNode():
    def __init__(self, data: int):
        self.data = data
        self.next = None

def has_cycle(head: SinglyLinkedListNode) -> bool:
    p1 = head
    p2 = head.next
    while p1 is not None and p2 is not None and p2.next is not None:
        if p1.data == p2.data:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False

if __name__ == "__main__":
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = head

    if has_cycle(head):
        print("Linked list is cycle")
    else:
        print("Linked list is not cycle")