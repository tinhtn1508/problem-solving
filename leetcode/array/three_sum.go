package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	out := make([][]int, 0)
	var i int = 0
	sort.Ints(nums)
	for i < len(nums) {
		num := nums[i]
		start := i + 1
		end := len(nums) - 1
		for start < end {
			curr := nums[start] + nums[end]
			if curr < -num {
				start++
			} else if curr > -num {
				end--
			} else {
				out = append(out, []int{num, nums[start], nums[end]})
				oldStart := start
				oldEnd := end
				for start > end && nums[start] == nums[oldStart] {
					start++
				}
				for end > start && nums[end] == nums[oldEnd] {
					end--
				}
				for i+1 < len(nums) && nums[i+1] == nums[i] {
					i++
				}
			}
		}
		i++
	}
	return out
}

func main() {
	data := []int{-1, 0, 1, 2, -1, -4}
	res := threeSum(data)

	for i := 0; i < len(res); i++ {
		for j := 0; j < len(res[0]); j++ {
			fmt.Printf("%d ", res[i][j])
		}
		fmt.Printf("\n")
	}
}
