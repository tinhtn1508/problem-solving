class Solution():
    def combine(self, n, k):
        res = []
        self.dfs(range(1, n+1), k, 0, [], res)
        return res
    def dfs(self, nums, k, index, path, res):
        if k == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)

print(Solution().combine(4, 3))