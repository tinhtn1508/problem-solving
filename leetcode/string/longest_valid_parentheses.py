class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans

if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))