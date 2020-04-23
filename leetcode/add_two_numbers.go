/*
 * Problem:
 *     - You are given two non-empty linked lists representing two non-negative integers.
 *     The digits are stored in reverse order and each of their nodes contain a single digit.
 *     Add the two numbers and return it as a linked list.
 *     - You may assume the two numbers do not contain any leading zerom expect the number 0 itself.
 * Example:
 *     - Input:(2 -> 4 -> 3) + (5 -> 6 -> 4)
 *     - Output: 7 -> 0 -> 8
 *     - Explanation: 342 + 465 = 807
 * Solution:
 *     - Traverse both lists and keep track of sum and carry for each digit
 * Cost:
 *     - Time: O(max(m, n))
 *     - Space: O(max(m, n))
 *     - m and n are lengths of two lists
 */
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	p1 := l1
	p2 := l2
	dummy := &ListNode{Val: 0, Next: nil}
	curr := dummy
	carry := 0

	for p1 != nil || p2 != nil {
		x, y := 0, 0
		if p1 != nil {
			x = p1.Val
		}
		if p2 != nil {
			y = p2.Val
		}
		sum := x + y + carry
		carry = sum / 10
		curr.Next = &ListNode{Val: sum % 10, Next: nil}
		curr = curr.Next
		if p1 != nil {
			p1 = p1.Next
		}
		if p2 != nil {
			p2 = p2.Next
		}
	}
	if carry > 0 {
		curr.Next = &ListNode{Val: carry, Next: nil}
	}
	return dummy.Next
}

func main() {
	l1 := &ListNode{Val: 2, Next: nil}
	l1.Next = &ListNode{Val: 4, Next: nil}
	l1.Next.Next = &ListNode{Val: 3, Next: nil}
	l2 := &ListNode{Val: 5, Next: nil}
	l2.Next = &ListNode{Val: 6, Next: nil}
	l2.Next.Next = &ListNode{Val: 4, Next: nil}

	result := addTwoNumbers(l1, l2)
	for result != nil {
		fmt.Printf("%d ", result.Val)
		result = result.Next
	}
	fmt.Printf("\n")
}
