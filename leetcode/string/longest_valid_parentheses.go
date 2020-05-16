package main

import (
	"fmt"
	"math"
)

func longestValidParentheses(s string) int {
	max := 0
	var stack []int
	stack = append(stack, -1)
	for i, c := range s {
		if c == 40 {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				max = int(math.Max(float64(max), float64(i-stack[len(stack)-1])))
			}
		}
	}
	return max
}

func main() {
	fmt.Println(longestValidParentheses(")()())"))
}
