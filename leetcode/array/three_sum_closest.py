'''
Problem:
    - Given an array nums of n integer and an integer target, find three integer in nums
    such that the sum is cloest to target. Return the sum of the three integer. You may assume
    that each input would have exactly on solution
Example:
    - nums = [-1, 2, 1, -4] and target = 1
    - The sums that is cloest to the target is 2. (-1 + 2 +1 = 2)
'''
import sys

def threeSumClosest(nums: list, target: int) -> int:
    closestSum = sys.maxsize
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            curr = nums[start] + nums[end] + nums[i]
            if abs(target - curr) < abs(target - closestSum):
                closestSum = curr
            if curr < target:
                start += 1
            else:
                end -= 1    
    return closestSum

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    print("The sums: {}".format(threeSumClosest(nums, 1)))