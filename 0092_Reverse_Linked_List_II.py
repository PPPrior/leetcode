""" Linked List """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        head = ListNode(-1, head)
        pre = head
        for i in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = next
        return head.next
