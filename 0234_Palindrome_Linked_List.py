""" Linked List """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals, curr = list(), head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1]
