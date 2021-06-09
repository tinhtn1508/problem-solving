class Solution():
    def permute(self, nums):
        def dfs(nums, path):
            print(nums, "----", path)
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        res = []
        dfs(nums, [])
        return res

print(Solution().permute([1, 2, 3]))