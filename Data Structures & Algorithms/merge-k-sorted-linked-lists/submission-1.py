# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for ls in lists:
            while ls:
                arr.append(ls.val)
                ls = ls.next
        
        arr.sort()
        head = ListNode()
        curr = head

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        
        return head.next