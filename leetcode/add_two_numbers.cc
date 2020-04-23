/*
 * Problem:
 *     - You are given two non-empty linked lists representing two non-negative integers.
 *     The digits are stored in reverse order and each of their nodes contain a single digit.
 *     Add the two numbers and return it as a linked list.
 *     - You may assume the two numbers do not contain any leading zerom expect the number 0 itself.
 * Example:
 *     - Input:(2 -> 4 -> 3) + (5 -> 6 -> 4)
 *     - Output: 7 -> 0 -> 8
 *     - Explanation: 342 + 465 = 807
 * Solution:
 *     - Traverse both lists and keep track of sum and carry for each digit
 * Cost:
 *     - Time: O(max(m, n)) 
 *     - Space: O(max(m, n))
 *     - m and n are lengths of two lists 
 */
#include <bits/stdc++.h>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

struct Solution {
    ListNode* addTwoNumber(ListNode* l1, ListNode* l2) {
        
        auto p1 = l1;
        auto p2 = l2;
        auto dummy = new ListNode(0);
        auto curr = dummy;
        int carry = 0;
        while (p1 != nullptr || p2 != nullptr) {
            int x = p1 != nullptr ? p1->val : 0;
            int y = p2 != nullptr ? p2->val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            p1 = p1 != nullptr ? p1->next : nullptr;
            p2 = p2 != nullptr ? p2->next : nullptr;
        }
        curr->next = carry > 0 ? new ListNode(carry) : nullptr;
        return dummy->next;
    }
};

int main() {
    auto l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    auto l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);
    auto result = Solution().addTwoNumber(l1, l2);
    while (result != nullptr) {
        std::cout << result->val << " ";
        result = result->next;
    }
    std::cout << std::endl;
}