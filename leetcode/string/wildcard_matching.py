class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        rows, cols = len(s), len(p)
        dp = [[False]*cols for _ in range(rows)]
        dp[0][0] = True
        for col in range(1, cols):
            if p[col] == "*":
                dp[0][col] = dp[0][col-1]
        for row in range(1, rows):
            for col in range(1, cols):
                if s[row] == p [col] or p[col] == '?':
                    dp[row][col] = dp[row-1][col-1]
                elif p[col] == '*':
                    dp[row][col] = dp[row][col-1] or dp[row-1][col]
        return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().isMatch("adceb", "*a*b"))