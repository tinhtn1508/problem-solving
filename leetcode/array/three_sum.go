package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [2][3]int {
	var out [2][3]int
	var i int = 0
	sort.Ints(nums)
	row := 0
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
				out[row][0] = num
				out[row][1] = nums[start]
				out[row][2] = nums[end]
				row++
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
