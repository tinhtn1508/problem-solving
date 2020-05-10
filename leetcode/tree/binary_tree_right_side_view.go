package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	var q []*TreeNode
	q = append(q, root)
	var res []int
	for len(q) != 0 {
		var inner []int
		size := len(q)
		for i := 0; i < size; i++ {
			tmp := q[0]
			q = q[1:]
			if tmp.Left != nil {
				q = append(q, tmp.Left)
			}
			if tmp.Right != nil {
				q = append(q, tmp.Right)
			}
			inner = append(inner, tmp.Val)
		}
		res = append(res, inner[len(inner)-1])
	}
	return res
}
func main() {
	root := &TreeNode{3, nil, nil}
	root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{20, nil, nil}
	root.Right.Left = &TreeNode{15, nil, nil}
	root.Right.Right = &TreeNode{7, nil, nil}
	out := rightSideView(root)
	fmt.Println(out)
}
