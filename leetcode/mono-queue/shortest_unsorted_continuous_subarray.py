'''
Problem

Given an integer array nums, you need to find one continuous subarray that
if you only sort this subarray in asecending order, then the whole array will
be sorted in ascending order.

Return the shortest such subarray and output its length
'''

'''
Solution #1
'''
def solution1(nums):
    l, r = len(nums), 0
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                l = min(l, i)
                r = max(r, j)
    return 0 if r - l < 0 else r - l + 1

print(solution1([2,6,4,8,10,9,15]))
print(solution1([2,6,7,8,10,9,15]))

'''
Solution #2
'''
def solution2(nums):
    nums_sorted = sorted(nums)
    start, end = len(nums), 0
    for i, v in enumerate(nums_sorted):
        if v != nums[i]:
            start = min(start, i)
            end = max(end, i)
    return 0 if end - start < 0 else end - start + 1

print(solution2([2,6,4,8,10,9,15]))
print(solution2([2,6,7,8,10,9,15]))