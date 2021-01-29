""" Two Pointers """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while True:
            if not (p1 and p1.next):
                return
            p1, p2 = p1.next.next, p2.next
            if p1 == p2:
                break
        p1 = head
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
