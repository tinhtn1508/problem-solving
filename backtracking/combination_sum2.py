
def combine(candidates, target):
    def dfs(nums, target, index, path):
        # print(target, index, path)
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            dfs(nums, target-nums[i], i+1, path+[nums[i]])
    res = []
    dfs(sorted(candidates), target, 0, [])
    return res

print(combine([2,3,6,3], 6))