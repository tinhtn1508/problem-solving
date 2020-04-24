/*
 * Problem:
 *  - A linked list is said to contain a cycle if any node is visited more than once while traversing the list
 * Solution:
 *  - Use two pointer to traverse, one is 1 step and another is 2 steps
 * Cost:
 * - O(n): n is length of linked list
 */
package main

import "fmt"

type SinglyLinkedListNode struct {
	Data int
	Next *SinglyLinkedListNode
}

func hasCycle(head *SinglyLinkedListNode) bool {
	p1 := head
	p2 := head.Next
	for p1 != nil && p2 != nil && p2.Next != nil {
		if p1.Data == p2.Data {
			return true
		}
		p1 = p1.Next
		p1 = p2.Next.Next
	}
	return false
}

func main() {
	head := &SinglyLinkedListNode{Data: 1, Next: nil}
	head.Next = &SinglyLinkedListNode{Data: 2, Next: nil}
	head.Next.Next = &SinglyLinkedListNode{Data: 3, Next: nil}
	head.Next.Next.Next = head.Next
	if hasCycle(head) {
		fmt.Println("Linked list is cycle")
	} else {
		fmt.Println("Linked list is not cycle")
	}
}
