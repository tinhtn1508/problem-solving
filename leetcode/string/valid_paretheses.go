package main

import "fmt"

func isValid(s string) bool {
	var mapping = make(map[string]string)
	mapping[")"] = "("
	mapping["}"] = "{"
	mapping["]"] = "["
	var stack []string
	for i := 0; i < len(s); i++ {
		if val, ok := mapping[string(s[i])]; ok {
			index := len(stack) - 1
			if index < 0 {
				return false
			}
			top := stack[index]
			stack = stack[:index]
			if val != top {
				return false
			}
		} else {
			stack = append(stack, string(s[i]))
		}
	}
	if len(stack) != 0 {
		return false
	}
	return true
}

func main() {
	fmt.Println(isValid("[]()"))
}
