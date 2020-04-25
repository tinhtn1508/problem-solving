package main

import (
	"fmt"
	"sort"
)

func main() {

	data := []struct {
		Frist  string
		Second int
	}{
		{"AA", 2},
		{"BB", 4},
		{"AA", 5},
		{"AA", 1},
	}

	sort.SliceStable(data, func(i, j int) bool {
		if data[i].Frist < data[j].Frist {
			return true
		}

		if data[i].Frist == data[j].Frist {
			return data[i].Second < data[j].Second
		}

		return false
	})

	for _, val := range data {
		fmt.Println(val.Frist, val.Second)
	}
}
