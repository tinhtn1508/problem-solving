'''
Problem:
    - There are two sorted arrays nums1 and nums2 of size m and n respectively
    - Find the median of the twoo sorted arrays. The overall run time complexity should
    be O(log(m+n))
Cost:
    - Complexity: O(log(min(m, n)))
    - Space: O(1)
'''
import sys

def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    imin, imax, haft_len = 0, m, (m + n + 1) / 2
    print("m: {}, n: {}, haft_len: {}".format(m, n, haft_len))
    while imin <= imax:
        print("imin = {}, imax = {}".format(imin, imax))
        i = int((imax + imin) / 2)
        j = int(haft_len - i)
        print("i = {}, j = {}".format(i, j))
        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])
            
            if (m + n) % 2 == 1:
                return max_of_left
            
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            
            return (max_of_left + min_of_right) / 2

if __name__ == "__main__":
    nums1 = [1, 7, 100]
    nums2 = [2, 8, 9, 10, 11]
    print("Median is {}".format(findMedianSortedArrays(nums1, nums2)))