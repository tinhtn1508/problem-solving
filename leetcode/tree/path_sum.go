package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}

	if sum == root.Val && root.Left == nil && root.Right == nil {
		return true
	}

	return hasPathSum(root.Left, sum-root.Val) || hasPathSum(root.Right, sum-root.Val)
}

func main() {
	root := &TreeNode{5, nil, nil}
	root.Left = &TreeNode{4, nil, nil}
	root.Right = &TreeNode{8, nil, nil}
	root.Left.Left = &TreeNode{11, nil, nil}
	root.Left.Left.Left = &TreeNode{7, nil, nil}
	root.Left.Left.Right = &TreeNode{2, nil, nil}
	root.Right.Left = &TreeNode{13, nil, nil}
	root.Right.Right = &TreeNode{4, nil, nil}
	root.Right.Right.Right = &TreeNode{1, nil, nil}
	fmt.Println(hasPathSum(root, 22))
	fmt.Println(hasPathSum(root, 27))
}
