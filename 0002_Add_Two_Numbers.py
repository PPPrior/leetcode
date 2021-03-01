""" Linked List """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        prev = head
        carry = 0
        while l1 or l2:
            m = l1.val if l1 else 0
            n = l2.val if l2 else 0
            sum = m + n + carry
            prev.next = ListNode(sum % 10)
            carry = sum // 10
            prev = prev.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        prev.next = ListNode(carry) if carry else None
        return head.next
