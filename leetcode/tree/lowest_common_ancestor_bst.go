package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	parent_val, p_val, q_val := root.Val, p.Val, q.Val
	if p_val > parent_val && q_val > parent_val {
		return lowestCommonAncestor(root.Right, p, q)
	} else if p_val < parent_val && q_val < parent_val {
		return lowestCommonAncestor(root.Left, p, q)
	} else {
		return root
	}
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
	q := &TreeNode{2, nil, nil}
	p := &TreeNode{4, nil, nil}
	res := lowestCommonAncestor(root, p, q)
	fmt.Println(res.Val)
}
