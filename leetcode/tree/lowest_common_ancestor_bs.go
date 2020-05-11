package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	var res *TreeNode
	helper(root, p, q, &res)
	return res
}

func helper(root, p, q *TreeNode, res **TreeNode) bool {
	if root == nil {
		return false
	}
	left := helper(root.Left, p, q, res)
	right := helper(root.Right, p, q, res)
	mid := root == p || root == q
	if (mid && left) || (mid && right) || (right && left) {
		*res = root
	}
	return mid || left || right
}

func main() {
	root := &TreeNode{6, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Right = &TreeNode{8, nil, nil}
	root.Right.Left = &TreeNode{7, nil, nil}
	root.Right.Right = &TreeNode{9, nil, nil}
	root.Left.Left = &TreeNode{0, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Left.Right.Left = &TreeNode{3, nil, nil}
	root.Left.Right.Right = &TreeNode{5, nil, nil}
	q := root.Left
	p := root.Left.Right
	res := lowestCommonAncestor(root, p, q)
	fmt.Println(res.Val)
}
