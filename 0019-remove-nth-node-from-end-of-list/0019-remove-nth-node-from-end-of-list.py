# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        tmp = head
        head_num = []
        while tmp:
            head_num.append(tmp.val)
            tmp = tmp.next
            count +=1
        curr = None
        if count == n:
            return head.next
        
        
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
