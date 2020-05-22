# Problem: https://leetcode.com/problems/unique-paths/
class Solution:
    def unique_path(self, m: int, n: int) -> int:
        dp = [[1 for rows in range(n)] for cols in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col - 1]
        return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().unique_path(3, 3))