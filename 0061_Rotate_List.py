""" Linked List """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        curr, n = head, 1
        while curr.next:
            curr = curr.next
            n += 1
        if k % n == 0:
            return head
        curr.next = head
        steps = n - k % n
        for _ in range(steps):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
