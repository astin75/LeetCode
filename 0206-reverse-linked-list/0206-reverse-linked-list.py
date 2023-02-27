# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr, prev = head, head
        curr = curr.next
        prev.next = None

        while curr:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext

        return prev   
            
            

        
