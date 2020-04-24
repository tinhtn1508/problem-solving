/*
 * Problem:
 *  - There are two sorted arrays nums1 and nums2 of size m and n respectively
 *  - Find the median of the twoo sorted arrays. The overall run time complexity should
 *  be O(log(m+n))
 * Example:
 *  - nums1 = [1, 3]
 *  - nums2 = [2]
 *  - the median is 2.0
 * Solution:
 *  - Use multiset container
 */
#include <bits/stdc++.h>

double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
    std::multiset<int> s;
    for (auto v : nums1) s.insert(v);
    for (auto v : nums2) s.insert(v);
    const int n = s.size();
    auto itr = s.begin();
    std::advance(itr, n / 2);
    int n1 = *itr;
    int n2 = *(--itr);
    if (n%2 == 1) return n1;
    return static_cast<double>(n1 + n2) / 2;
}

int main() {
    std::vector<int> nums1 {1, 3};
    std::vector<int> nums2 {2};
    std::cout << "The median is: " << findMedianSortedArrays(nums1, nums2) << std::endl;
    return 0;
}