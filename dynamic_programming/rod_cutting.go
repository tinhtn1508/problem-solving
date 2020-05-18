package main

import (
	"fmt"
	"math"
)

func cut_rod(p []int64, n int64) int64 {
	if n == 0 {
		return 0
	}
	var q int64
	var i int64
	for ; i < n; i++ {
		q = int64(math.Max(float64(q), float64(p[i]+cut_rod(p, n-i-1))))
	}
	return q
}

func rut_rod_optimal(p []int64, n int64) int64 {
	r := make([]int64, len(p))
	return memorized_cut_rod_aux(p, n, r)
}

func memorized_cut_rod_aux(p []int64, n int64, r []int64) int64 {
	if n <= 0 {
		return 0
	}
	if r[n-1] > 0 {
		return r[n-1]
	}
	var q int64
	var i int64
	i = 0
	for ; i < n; i++ {
		q = int64(math.Max(float64(q), float64(p[i]+memorized_cut_rod_aux(p, n-i-1, r))))
	}
	r[n-1] = q
	return q
}

func bottom_up_cut_rod(p []int64, n int64) int64 {
	r := make([]int64, len(p)+1)
	var i int64
	for ; i < n; i++ {
		q := int64(0)
		for j := int64(0); j <= i; j++ {
			q = int64(math.Max(float64(q), float64(p[j]+r[i-j])))
		}
		r[i+1] = q
	}
	return r[n]
}

func main() {
	p := []int64{1, 5, 8, 9, 10, 17, 17, 20, 24, 30}
	fmt.Println(cut_rod(p, 3))
	fmt.Println(rut_rod_optimal(p, 3))
	fmt.Println(bottom_up_cut_rod(p, 3))
}
