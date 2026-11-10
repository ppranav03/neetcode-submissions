# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
    
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev will be our new head reversed
        head = prev
        curr = prev
        prev = None
        for i in range(1, n):
            prev = curr
            curr = curr.next
        
        if n == 1:
            head = head.next
        else:
            prev.next = curr.next

        prev = None
        curr = head
    
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        


