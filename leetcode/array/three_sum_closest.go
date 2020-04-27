/*
 * Problem:
 *     - Given an array nums of n integer and an integer target, find three integer in nums
 *     such that the sum is cloest to target. Return the sum of the three integer. You may assume
 *     that each input would have exactly on solution
 * Example:
 *     - nums = [-1, 2, 1, -4] and target = 1
 *     - The sums that is cloest to the target is 2. (-1 + 2 +1 = 2)
 */
package main

import (
	"fmt"
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closestSum := int(^uint(0) >> 1)
	for i := 0; i < len(nums)-2; i++ {
		start := i + 1
		end := len(nums) - 1
		for start < end {
			curr := nums[start] + nums[end] + nums[i]
			if math.Abs(float64(curr-target)) < math.Abs(float64(target-closestSum)) {
				closestSum = curr
			}
			if curr < target {
				start++
			} else {
				end--
			}
		}
	}
	return closestSum
}

func main() {
	nums := []int{-1, 2, 1, -4}
	fmt.Printf("The sums: %d\n", threeSumClosest(nums, 1))
}
