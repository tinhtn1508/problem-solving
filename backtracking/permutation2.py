class Solution():
    def permute(self, nums):
        def dfs(nums, path):
            if len(nums) == len(path):
                res.append(path)
                return
            for i in range(len(nums)):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:
                        continue
                    visited[i] = True
                    dfs(nums, path+[nums[i]])
                    visited[i] = False
        res = []
        visited = [False]*len(nums)
        dfs(sorted(nums), [])
        return res

print(Solution().permute([1, 2, 1]))