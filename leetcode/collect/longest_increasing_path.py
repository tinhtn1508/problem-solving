from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        self.m, self.n = len(matrix), len(matrix[0])
        self.move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.cache = {}
        self.numMax = 0
        for i in range(self.m):
            for j in range(self.n):
                self.__dfs(matrix, i, j, -1)
        return self.numMax
    
    def __dfs(self, matrix, i, j, prev):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return -1
        if matrix[i][j] <= prev:
            return -1
        
        if (i, j) not in self.cache:
            num = 0
            for imov, jmov in self.move:
                num = max(num, self.__dfs(matrix, i + imov, j + jmov, matrix[i][j]))
            self.cache[(i, j)] = num + 1
            self.numMax = max(self.numMax, self.cache[(i, j)])
        return self.cache[(i, j)]


if __name__ == "__main__":
    nums = [[9, 9, 4],[6, 6, 8], [2, 1, 1]]
    print(Solution().longestIncreasingPath(nums))