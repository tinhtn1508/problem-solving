/*
Problem:
Write a function:
    def solution(a : list) ->int:
that, given an array A consisting of N integers, returns the maximun sum of
two numbers whose digits add up to an equal sum. If there are no two numbers
whose digits have an equal sum, the function should return -1.
Example:
    A = [51, 71, 17, 42], the function should return 93. There are two pair
    of numbers whose digits add up to an equal sum: (51, 42) and (17, 71).
    The first pair sums up to 93.
*/
package main

import (
	"fmt"
	"math"
)

func digit_sum(num int) int {
	val := 0
	for num != 0 {
		val += num % 10
		num /= 10
	}
	return val
}

func solution(nums []int) int {
	m := make(map[int]int)
	max_val := -1
	for _, num := range nums {
		digit_sum_ := digit_sum(num)
		if val, ok := m[digit_sum_]; ok {
			max_val = int(math.Max(float64(max_val), float64(val+num)))
		} else {
			m[digit_sum_] = num
		}
	}
	return max_val
}

func main() {
	fmt.Println(solution([]int{51, 71, 17, 42}))
	fmt.Println(solution([]int{42, 60, 33, 42}))
	fmt.Println(solution([]int{51, 32, 43}))
}
