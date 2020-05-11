package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {
	var res []string
	helper(root, "", &res)
	return res
}

func helper(root *TreeNode, str string, out *[]string) {
	if root.Left == nil && root.Right == nil {
		str += strconv.Itoa(root.Val)
		*out = append(*out, str)
		return
	}
	str += strconv.Itoa(root.Val) + "->"
	if root.Left != nil {
		helper(root.Left, str, out)
	}
	if root.Right != nil {
		helper(root.Right, str, out)
	}
}

func main() {
	root := &TreeNode{3, nil, nil}
	root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{20, nil, nil}
	root.Right.Left = &TreeNode{15, nil, nil}
	root.Right.Right = &TreeNode{7, nil, nil}
	out := binaryTreePaths(root)
	fmt.Println(out)
}
