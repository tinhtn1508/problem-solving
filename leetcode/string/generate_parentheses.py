from typing import List

class Solution:
    # By Brute-Force
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        def valid(A):
            bal = 0
            for c in A:
                if c == '(' :
                    bal += 1
                else:
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        ans = []
        generate()
        return ans
    def generateParenthesis2(self, n: int):
        ans = []
        def backtrack(S='', left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()
        return ans

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis2(3))
