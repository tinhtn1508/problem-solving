package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	return solve(root, -1, -1)
}

func solve(node *TreeNode, lower int, upper int) bool {
	if node == nil {
		return true
	}
	if lower != -1 && node.Val <= lower {
		return false
	}
	if upper != -1 && node.Val >= upper {
		return false
	}
	if !solve(node.Right, node.Val, upper) {
		return false
	}
	if !solve(node.Left, lower, node.Val) {
		return false
	}
	return true
}

func main() {
	root := &TreeNode{2, nil, nil}
	root.Left = &TreeNode{1, nil, nil}
	root.Right = &TreeNode{3, nil, nil}
	if isValidBST(root) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
