# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    successor = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverseN(self, head: ListNode, n: int):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last
