def threeSum(nums: list) -> list:
    nums = sorted(nums)
    out = []
    i = 0
    while i < len(nums):
        num = nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            curr = nums[start] + nums[end]
            if curr < -num:
                start += 1
            elif curr > -num:
                end -= 1
            else:
                out.append([num, nums[start], nums[end]])
                old_start = start
                old_end = end
                while start < end and nums[start] == nums[old_start]:
                    start += 1
                while end > start and nums[end] == nums[old_end]:
                    end -= 1
                while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                    i += 1
        i += 1
    return out

if __name__ == "__main__":
    data = [-1, 0, 1, 2, -1, -4]
    result = threeSum(data)
    print(result)