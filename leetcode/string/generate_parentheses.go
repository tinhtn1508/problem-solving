package main

import "fmt"

func generateParenthesis(n int) []string {
	var out []string
	backtrack("", n, 0, 0, &out)
	return out
}

func backtrack(s string, n, left, right int, out *[]string) {
	if len(s) == 2*n {
		*out = append(*out, s)
		return
	}
	if left < n {
		backtrack(s+"(", n, left+1, right, out)
	}
	if right < left {
		backtrack(s+")", n, left, right+1, out)
	}
}

func main() {
	fmt.Println(generateParenthesis(4))
}