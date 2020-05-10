package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BSTIterator struct {
	Arr []int
}

func Constructor(root *TreeNode) BSTIterator {
	bst := BSTIterator{}
	bst.helper(root)
	return bst
}

func (this *BSTIterator) helper(root *TreeNode) {
	if root == nil {
		return
	}
	this.helper(root.Left)
	this.Arr = append(this.Arr, root.Val)
	this.helper(root.Right)
}

/** @return the next smallest number */
func (this *BSTIterator) Next() int {
	tmp := this.Arr[0]
	this.Arr = this.Arr[1:]
	return tmp
}

/** @return whether we have a next smallest number */
func (this *BSTIterator) HasNext() bool {
	return len(this.Arr) != 0
}

func main() {
	root := &TreeNode{Val: 7, Left: nil, Right: nil}
	root.Left = &TreeNode{Val: 3, Left: nil, Right: nil}
	root.Right = &TreeNode{Val: 15, Left: nil, Right: nil}
	root.Right.Left = &TreeNode{Val: 9, Left: nil, Right: nil}
	root.Right.Right = &TreeNode{Val: 20, Left: nil, Right: nil}

	bst := Constructor(root)
	for i := 0; i < 5; i++ {
		fmt.Println(bst.Next())
		fmt.Println(bst.HasNext())
	}
}
