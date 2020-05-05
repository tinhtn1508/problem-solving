package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	out := 999999999
	solve(root, 1, &out)
	return out
}

func solve(root *TreeNode, level int, out *int) {
	if root == nil {
		return
	}

	if root.Left == nil && root.Right == nil {
		if *out > level {
			*out = level
		}
		return
	}
	solve(root.Left, level+1, out)
	solve(root.Right, level+1, out)
}

func main() {
	root := &TreeNode{1, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Right = &TreeNode{2, nil, nil}
	root.Left.Left = &TreeNode{3, nil, nil}
	// root.Left.Right = &TreeNode{4, nil, nil}
	root.Right.Left = &TreeNode{4, nil, nil}
	root.Right.Right = &TreeNode{3, nil, nil}
	min := minDepth(root)
	fmt.Println(min)
}
