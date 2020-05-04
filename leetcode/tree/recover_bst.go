package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

var first = true
var parent = &TreeNode{MinInt, nil, nil}

func recoverTree(root *TreeNode) {
	arr := make([]*TreeNode, 2)
	arr[0], arr[1] = nil, nil
	solve(root, arr)
	arr[0].Val, arr[1].Val = arr[1].Val, arr[0].Val
}

func solve(root *TreeNode, arr []*TreeNode) {
	if root == nil {
		return
	}
	solve(root.Left, arr)
	if root.Val <= parent.Val {
		if first == true {
			arr[0] = parent
			first = false
		}
		arr[1] = root
	}
	parent = root
	solve(root.Right, arr)
}

func main() {
	root := &TreeNode{3, nil, nil}
	root.Left = &TreeNode{1, nil, nil}
	root.Right = &TreeNode{4, nil, nil}
	root.Right.Left = &TreeNode{2, nil, nil}
	recoverTree(root)
	fmt.Printf("%d, %d, %d, %d\n", root.Val, root.Left.Val, root.Right.Val, root.Right.Left.Val)
}
