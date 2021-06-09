
class Solution():
    def subset1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    def dfs(self, nums, index, path, res):
        print(nums, index, path, res)
        res.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i-1] == nums[i]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()

print(Solution().subset1([1,2,2]))