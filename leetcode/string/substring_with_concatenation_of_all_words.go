package main

import "fmt"

func findSubstring(s string, words []string) []int {
	if len(words) == 0 || s == "" {
		return nil
	}
	lw, lws, ls := len(words[0]), len(words), len(s)
	totallen := lw * lws
	if ls < totallen {
		return nil
	}
	var rst []int
	ct := counter(words)
	for i := 0; i < ls-totallen+1; i++ {
		ctt, j := make(map[string]int), 0
		for j < lws {
			curr := s[i+j*lw : i+(j+1)*lw]
			if _, ok := ctt[curr]; ok {
				ctt[curr]++
			} else {
				ctt[curr] = 1
			}

			if ctt[curr] > ct[curr] {
				break
			}
			j++
		}
		if j == lws {
			rst = append(rst, i)
		}
	}
	return rst
}

func counter(words []string) map[string]int {
	m := make(map[string]int)
	for _, word := range words {
		if _, ok := m[word]; ok {
			m[word]++
		} else {
			m[word] = 1
		}
	}
	return m
}

func main() {
	words := []string{"foo", "bar"}
	fmt.Println(findSubstring("barfoothefoobarman", words))
}
