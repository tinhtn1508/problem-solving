package main

import "fmt"

func isMatch(s string, p string) bool {
	s = " " + s
	p = " " + p
	rows, cols := len(s), len(p)
	dp := make([][]bool, rows)
	for i := range dp {
		dp[i] = make([]bool, cols)
	}
	dp[0][0] = true
	for col := 1; col < cols; col++ {
		if p[col] == 42 {
			dp[0][col] = dp[0][col-1]
		}
	}

	for row := 1; row < rows; row++ {
		for col := 1; col < cols; col++ {
			if s[row] == p[col] || p[col] == 63 {
				dp[row][col] = dp[row-1][col-1]
			} else if p[col] == 42 {
				dp[row][col] = dp[row-1][col] || dp[row][col-1]
			}
		}
	}
	return dp[rows-1][cols-1]
}

func main() {
	fmt.Println(isMatch("adceb", "*a*b"))
}
