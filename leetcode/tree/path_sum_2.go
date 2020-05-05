package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, sum int) [][]int {
	var path []int
	var out [][]int
	solve(root, sum, path, &out)
	return out
}

func solve(root *TreeNode, sum int, path []int, out *[][]int) {
	if root == nil {
		return
	}

	tmp := make([]int, len(path))
	copy(tmp, path)
	tmp = append(tmp, root.Val)

	if sum == root.Val && root.Left == nil && root.Right == nil {
		*out = append(*out, tmp)
		return
	}
	solve(root.Left, sum-root.Val, tmp, out)
	solve(root.Right, sum-root.Val, tmp, out)
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
	root.Right.Right.Left = &TreeNode{5, nil, nil}
	// fmt.Println(pathSum(root, 22))
	fmt.Println(pathSum(root, 22))
}
