package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	var maxs = -99999999
	helper(root, &maxs)
	return maxs
}

func helper(root *TreeNode, maxs *int) int {
	ls := 0
	rs := 0
	if root.Left == nil && root.Right == nil {
		*maxs = max(*maxs, root.Val)
		return root.Val
	}
	if root.Left != nil {
		ls = helper(root.Left, maxs)
	}
	if root.Right != nil {
		rs = helper(root.Right, maxs)
	}
	if ls >= 0 && rs >= 0 {
		*maxs = max(*maxs, root.Val+ls+rs)
		return root.Val + max(ls, rs)
	} else if ls >= 0 && rs < 0 {
		*maxs = max(*maxs, root.Val+ls)
		return root.Val + ls
	} else if ls < 0 && rs >= 0 {
		*maxs = max(*maxs, root.Val+rs)
		return root.Val + rs
	} else {
		*maxs = max(*maxs, root.Val)
		return root.Val
	}
}

func max(t1, t2 int) int {
	if t1 < t2 {
		return t2
	}
	return t1
}

func main() {
	root := &TreeNode{Val: -10, Left: nil, Right: nil}
	root.Left = &TreeNode{Val: 9, Left: nil, Right: nil}
	root.Right = &TreeNode{Val: 20, Left: nil, Right: nil}
	root.Right.Left = &TreeNode{Val: 15, Left: nil, Right: nil}
	root.Right.Right = &TreeNode{Val: 7, Left: nil, Right: nil}
	fmt.Println(maxPathSum(root))
}
