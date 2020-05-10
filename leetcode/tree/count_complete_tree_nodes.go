package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var res int
	helper(root, &res)
	return res
}

func helper(root *TreeNode, res *int) {
	if root == nil {
		return
	} else {
		*res++
	}
	helper(root.Left, res)
	helper(root.Right, res)
}

func main() {
	root := &TreeNode{3, nil, nil}
	root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{20, nil, nil}
	root.Right.Left = &TreeNode{15, nil, nil}
	root.Right.Right = &TreeNode{7, nil, nil}
	out := countNodes(root)
	fmt.Println(out)
}
