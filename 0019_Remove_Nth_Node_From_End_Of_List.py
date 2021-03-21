""" Two Pointers """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not (head and head.next):
            return None
        p1, p2 = head, head
        for i in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        while p1:
            p1, p2 = p1.next, p2.next
            p2.next = p2.next.next
        return head
