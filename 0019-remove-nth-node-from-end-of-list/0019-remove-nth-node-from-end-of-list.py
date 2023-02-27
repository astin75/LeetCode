# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        head_num = []
        while head:
            head_num.append(head.val)
            head = head.next
            count +=1
        curr = None
        for idx, i in enumerate(head_num):
            target_count = count - idx
            if target_count == n:
                pass
            else:
                if not curr:
                    curr = ListNode(i)
                    curr_node = curr        
                else:
                    curr_node.next = ListNode(i)
                    curr_node = curr_node.next
        return curr      
