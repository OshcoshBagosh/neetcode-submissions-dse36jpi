# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Reverse 2 lists
        curr1, curr2 = l1, l2
        prev1, prev2 = None, None
        num1, num2 = 0, 0

        while curr1:
            temp = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp

        while curr2:
            temp = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = temp

        while prev1:
            num1 = num1 * 10 + prev1.val
            prev1 = prev1.next
        
        while prev2:
            num2 = num2 * 10 + prev2.val
            prev2 = prev2.next
        
        total = num1 + num2
        head = ListNode(0)
        curr = head

        while True:
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total //= 10
            if total == 0:
                break
        
        return head.next






