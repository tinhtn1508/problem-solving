package main

import "fmt"

func binarySearch(arr []int, left int, right int, x int) int {
	if left <= right {
		var mid int = left + (right-left)/2
		if arr[mid] == x {
			return mid
		}

		if arr[mid] > x {
			return binarySearch(arr, left, mid-1, x)
		}

		return binarySearch(arr, mid+1, right, x)
	}
	return -1
}

/* Execute:
 * go build binary_sreach.go
 * ./binary_sreach
 */
func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	x := 7
	result := binarySearch(arr, 0, len(arr), x)
	fmt.Printf("Index of %d: %d\n", x, result)
}
