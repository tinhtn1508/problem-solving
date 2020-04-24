/*
 * Problem:
 *  - A linked list is said to contain a cycle if any node is visited more than once while traversing the list
 * Solution:
 *  - Use two pointer to traverse, one is 1 step and another is 2 steps
 * Cost:
 * - O(n): n is length of linked list
 */
#include <bits/stdc++.h>

struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode* next;
    SinglyLinkedListNode(int data) : data(data), next(nullptr) {}
};

bool has_cycle(SinglyLinkedListNode* head) {
    auto p1 = head;
    auto p2 = head->next;

    while (p1 && p2 && p2->next)
    {
        if (p1->data == p2->data) return true;
        p1 = p1->next;
        p2 = p2->next->next;
    }
    return false;
}

int main() {
    auto head = new SinglyLinkedListNode(1);
    head->next = new SinglyLinkedListNode(2);
    head->next->next = new SinglyLinkedListNode(3);
    head->next->next->next = new SinglyLinkedListNode(4);
    head->next->next->next->next = head->next;
    
    if (has_cycle(head)) {
        std::cout << "Linked list is cycle\n";
    } else {
        std::cout << "Linked list is not cycle\n";
    }
    return 0;
}
