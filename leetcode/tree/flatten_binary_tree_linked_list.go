package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	var path []int
	solve(root, &path)
	if path != nil {
		path = path[1:]
		for len(path) != 0 {
			if root != nil {
				root.Left = nil
				root.Right = &TreeNode{path[0], nil, nil}
				root = root.Right
				path = path[1:]
			}
		}
	}
}

func solve(root *TreeNode, path *[]int) {
	if root == nil {
		return
	}
	*path = append(*path, root.Val)
	solve(root.Left, path)
	solve(root.Right, path)
}

func main() {
	root := &TreeNode{1, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Left.Left = &TreeNode{3, nil, nil}
	root.Left.Right = &TreeNode{4, nil, nil}
	root.Right = &TreeNode{5, nil, nil}
	root.Right.Right = &TreeNode{6, nil, nil}
	flatten(root)
	for root != nil {
		fmt.Println(root.Val)
		root = root.Right
	}
}
