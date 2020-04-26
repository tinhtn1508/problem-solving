/*
 * Problem:
 *    - There are two sorted arrays nums1 and nums2 of size m and n respectively
 *    - Find the median of the twoo sorted arrays. The overall run time complexity should
 *    be O(log(m+n))
 * Cost:
 *    - Complexity: O(log(min(m, n)))
 *    - Space: O(1)
 */
package main

import (
	"fmt"
)

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findMedianTwoSortedArrays(nums1, nums2 []int) float64 {
	m, n := len(nums1), len(nums2)
	if m > n {
		m, n, nums1, nums2 = n, m, nums2, nums1
	}
	imin, imax, haft := 0, m, (m+n+1)/2.0
	for imin <= imax {
		i := ((imax - imin) / 2)
		j := int(haft - i)
		if i < m && nums2[j-1] > nums1[i] {
			imin = i + 1
		} else if i > 0 && nums1[i-1] > nums2[j] {
			imax = i - 1
		} else {
			var max_of_left int
			if i == 0 {
				max_of_left = nums2[j-1]
			} else if j == 0 {
				max_of_left = nums1[i-1]
			} else {
				max_of_left = max(nums1[i-1], nums2[j-1])
			}
			if (m+n)%2 == 1 {
				return float64(max_of_left)
			}
			var max_of_right int
			if i == m {
				max_of_right = nums2[j]
			} else if j == n {
				max_of_right = nums1[i]
			} else {
				max_of_right = min(nums2[j], nums1[i])
			}
			return (float64(max_of_right) + float64(max_of_left)) / 2.0
		}
	}
	return -1.0
}

func main() {
	nums1 := []int{10, 100}
	nums2 := []int{1, 2, 3, 4}
	median := findMedianTwoSortedArrays(nums1, nums2)
	fmt.Printf("Median is %f\n", median)
}
