package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var nums [][]int
	var arr []int
	helper(root, arr, &nums)

	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += sliceToInt(nums[i])
	}
	return sum
}

func sliceToInt(s []int) int {
	res := 0
	op := 1
	for i := len(s) - 1; i >= 0; i-- {
		res += s[i] * op
		op *= 10
	}
	return res
}

func helper(root *TreeNode, arr []int, out *[][]int) {
	tmp := make([]int, len(arr))
	copy(tmp, arr)
	tmp = append(tmp, root.Val)
	if root.Left == nil && root.Right == nil {
		*out = append(*out, tmp)
		return
	}
	if root.Left != nil {
		helper(root.Left, tmp, out)
	}
	if root.Right != nil {
		helper(root.Right, tmp, out)
	}
}

func main() {
	root := &TreeNode{4, nil, nil}
	root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{0, nil, nil}
	root.Left.Left = &TreeNode{5, nil, nil}
	root.Left.Right = &TreeNode{1, nil, nil}
	fmt.Println(sumNumbers(root))
}
