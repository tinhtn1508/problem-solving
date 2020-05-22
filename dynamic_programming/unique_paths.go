package main

import "fmt"

func uniquePaths(m int, n int) int {
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			dp[row][col] = 1
		}
	}
	for row := 1; row < m; row++ {
		for col := 1; col < n; col++ {
			dp[row][col] = dp[row-1][col] + dp[row][col-1]
		}
	}
	return dp[m-1][n-1]
}

func main() {
	fmt.Println(uniquePaths(3, 2))
}
