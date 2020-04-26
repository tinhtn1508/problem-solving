/*
 * Problem: Given an array nums of n integers, are there elements a, b, c in nums such that
 * a + b + c = 0 ? Find all unique triplets in the array which gives the sum of zero
 * Solution:
 * 
 * Cost:
 *      - Complexity: O(n^2)
 *      - Space: O(2n)
 */

#include <bits/stdc++.h>

std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> out;
    int i = 0;
    while (i < nums.size()) {
        int num = nums[i];
        int start = i + 1;
        int end = nums.size() - 1;
        while (start < end) {
            int curr = nums[start] + nums[end];
            if (curr < -num) start += 1;
            else if (curr > -num) end -= 1;
            else {
                std::vector<int> tmp {num, nums[start], nums[end]};
                out.emplace_back(tmp);
                int old_start = start;
                int old_end = end;
                while (start <  end && nums[start] == nums[old_start]) start += 1;
                while (end > start && nums[end] == nums[old_end]) end -= 1;
                while (i + 1 < nums.size() && nums[i + 1] == nums[i]) i += 1;
            }
        }
        i += 1;
    }
    return out;
}

int main() {
    std::vector<int> vec {-1, 0, 1, 2, -1, -4};
    auto result = threeSum(vec);
    for (const auto & col : result) {
        for (int v : col) {
            std::cout << v << " ";
        }
        std::cout << std::endl;
    }
}