# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return
        
        prev = root = ListNode(None)
        prev.next = head
        
        while head and head.next:
            nex = head.next
            head.next = nex.next
            nex.next =  head
            prev.next= nex
            
            head = head.next
            prev = prev.next.next
            
        return root.next