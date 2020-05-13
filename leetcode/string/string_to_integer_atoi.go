package main

import (
	"fmt"
	"math"
	"strings"
	"unicode"
)

var max_range = int(math.Pow(2, 31))

func myAtoi(str string) int {
	str = strings.TrimSpace(str)
	var nums []int
	sign := false
	flag := false
	for _, c := range str {
		if c == 48 && len(nums) == 0 {
			flag = true
			continue
		}

		if c == 48 && len(nums) == 1 && (nums[0] == 45 || nums[0] == 43) {
			continue
		}

		if unicode.IsDigit(c) {
			nums = append(nums, int(c-48))
		} else if c == 45 && len(nums) == 0 {
			nums = append(nums, int(c))
			sign = true
			if flag == true {
				return 0
			}
		} else if c == 43 && len(nums) == 0 {
			nums = append(nums, int(c))
			continue
		} else {
			break
		}
	}
	num := 0
	if len(nums) > 0 {
		if nums[0] == 43 || nums[0] == 45 {
			nums = nums[1:]
		}
	}

	if len(nums) > 10 {
		if sign == true {
			return -max_range
		} else {
			return max_range - 1
		}
	}

	for i := len(nums) - 1; i >= 0; i-- {
		num += nums[len(nums)-1-i] * int(math.Pow10(i))
	}

	if sign == true {
		if num > max_range {
			return -max_range
		}
		return -num
	} else {
		if num > max_range-1 {
			return max_range - 1
		}
		return num
	}
}

func main() {
	fmt.Println(myAtoi("42"))
	fmt.Println(myAtoi("words and 987"))
	fmt.Println(myAtoi("   -42"))
	fmt.Println(myAtoi("-91283472332"))

}
