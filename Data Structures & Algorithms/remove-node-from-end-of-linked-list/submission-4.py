# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Reverse the list
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_head = prev

        if n == 1:
            reversed_head = reversed_head.next
        else:
            curr = reversed_head
            for i in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next

        prev = None
        curr = reversed_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev