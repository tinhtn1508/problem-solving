package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func solve(root *TreeNode, d int) int {
	if root == nil {
		return d
	}
	d++
	t1 := solve(root.Left, d)
	t2 := solve(root.Right, d)
	if t1 > t2 {
		return t1
	} else {
		return t2
	}
}

func maxDepth(root *TreeNode) int {
	return solve(root, 0)
}

func main() {
	root := &TreeNode{3, nil, nil}
	// root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{20, nil, nil}
	root.Right.Left = &TreeNode{15, nil, nil}
	root.Right.Right = &TreeNode{7, nil, nil}
	depth := maxDepth(root)
	fmt.Printf("max depth: %d\n", depth)
}
