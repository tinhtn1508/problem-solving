#include <bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    bool operator<(const ListNode &other) const
    {
        return val < other.val;
    }
};

struct Compare {
    bool operator()(std::pair<int, ListNode*> lhs, std::pair<int, ListNode*> rhs) {
        return lhs.first > rhs.first;
    }
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        auto head = new ListNode();
        auto point = head;
        std::priority_queue<std::pair<int, ListNode*>, std::vector<std::pair<int, ListNode*>>, Compare> pqueue;
        for (const auto& l : lists) {
            pqueue.push(std::make_pair(l->val, l));
        }

        while (!pqueue.empty()) {
            auto e = pqueue.top();
            pqueue.pop();
            point->next = new ListNode(e.first);
            point = point->next;
            auto tmp = e.second;
            tmp = tmp->next;
            if (tmp) {
                pqueue.push(std::make_pair(tmp->val, tmp));
            }
        }
        return head->next;
    }
};

int main() {
    auto l1 = new ListNode(1);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(5);

    auto l2 = new ListNode(1);
    l2->next = new ListNode(3);
    l2->next->next = new ListNode(4);

    auto l3 = new ListNode(2);
    l3->next = new ListNode(6);
    l3->next->next = new ListNode(7);

    std::vector<ListNode*> lists = {l1, l2, l3};
    auto res = Solution().mergeKLists(lists);

    while (res) {
        std::cout << res->val << std::endl;
        res = res->next;
    }
}
