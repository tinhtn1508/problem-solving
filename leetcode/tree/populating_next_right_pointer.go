package main

import "fmt"

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	var q []*Node
	q = append(q, root)
	for len(q) != 0 {
		size := len(q)
		var pre *Node

		for i := 0; i < size; i++ {
			tmp := q[0]
			q = q[1:]
			if pre != nil {
				pre.Next = tmp
			}
			if tmp.Left != nil {
				q = append(q, tmp.Left)
			}
			if tmp.Right != nil {
				q = append(q, tmp.Right)
			}
			pre = tmp
		}
	}
	return root
}

func main() {
	root := &Node{Val: 1, Left: nil, Right: nil, Next: nil}
	root.Left = &Node{Val: 2, Left: nil, Right: nil, Next: nil}
	root.Right = &Node{Val: 3, Left: nil, Right: nil, Next: nil}
	root.Left.Left = &Node{Val: 4, Left: nil, Right: nil, Next: nil}
	root.Left.Right = &Node{Val: 5, Left: nil, Right: nil, Next: nil}
	root.Right.Left = &Node{Val: 6, Left: nil, Right: nil, Next: nil}
	root.Right.Right = &Node{Val: 7, Left: nil, Right: nil, Next: nil}
	res := connect(root)
	for res != nil {
		curr := res
		for curr != nil {
			fmt.Println(curr.Val)
			curr = curr.Next
		}
		res = res.Left
	}
}
