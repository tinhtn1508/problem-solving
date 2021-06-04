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

'''
Solution #3
'''

class Solution:
    def difference(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = firstList
        for i in secondList:
            a = self.single(a, [i])
        return a
    
    def single(self, avails, booked):
        intervals = []
        i, j = 0, 0
        while i < len(avails) and j < len(booked):
            lo = max(avails[i][0], booked[j][0])
            hi = min(avails[i][1], booked[j][1])
            if lo <= hi:
                if lo == booked[j][0]:
                    if avails[i][0] != booked[j][0]:
                        intervals.append([avails[i][0], booked[j][0]])
                if hi == booked[j][1]:
                    if booked[j][1] != avails[i][1]:
                        intervals.append([booked[j][1], avails[i][1]])
            else:
                intervals.append(avails[i])
            if avails[i][1] < booked[j][1]:
                i += 1
            else:
                j += 1
        for t in range(i+1, len(avails)):
            intervals.append(avails[t])
        
        return intervals
