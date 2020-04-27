package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var result []int

func inorderTraversal(root *TreeNode) {
	if root == nil {
		return
	}
	inorderTraversal(root.Left)
	result = append(result, root.Val)
	inorderTraversal(root.Right)
}

func main() {
	root := &TreeNode{Val: 1, Left: nil, Right: nil}
	root.Left = &TreeNode{Val: 2, Left: nil, Right: nil}
	root.Right = &TreeNode{Val: 3, Left: nil, Right: nil}
	root.Right.Left = &TreeNode{Val: 4, Left: nil, Right: nil}
	inorderTraversal(root)
	for _, val := range result {
		fmt.Printf("%d ", val)
	}
	fmt.Println()
}
