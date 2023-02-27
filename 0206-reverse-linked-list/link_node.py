# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head = ListNode(5)
curr_node = head

curr_node.next = ListNode(4)
curr_node = curr_node.next

curr_node.next = ListNode(3)
curr_node = curr_node.next

curr_node.next = ListNode(2)
curr_node = curr_node.next

curr_node.next = ListNode(1)
curr_node = curr_node.next

while head:
    print(head.val)
    head = head.next
    