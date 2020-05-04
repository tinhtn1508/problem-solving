package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p != nil && q != nil {
		if p.Val != q.Val {
			return false
		} else {
			return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
		}
	}

	return false
}

func main() {
	p := &TreeNode{3, nil, nil}
	p.Left = &TreeNode{1, nil, nil}
	p.Right = &TreeNode{4, nil, nil}
	q := &TreeNode{3, nil, nil}
	q.Left = &TreeNode{1, nil, nil}
	q.Right = &TreeNode{2, nil, nil}
	if isSameTree(p, q) {
		fmt.Println("Same")
	} else {
		fmt.Println("Not same")
	}
}
