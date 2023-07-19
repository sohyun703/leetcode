# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def reverseBetween(self, head, left, right):
        if head is not None:
            return
        
        root=head
        prev , node = None, head
        cnt = 1
        
        if cnt<left:
            prev= node
            node = node.next
            cnt+=1
        
        reversed_head = prev #[1,2,3,4,5] #left2, right4 일때 prev -> 1
        reversed_tail = node #node = 2
        
        if cnt<= right:
            next,node.next = node.next,prev
            prev,node = node,next
            cnt+=1
        
        if reversed_head: #1
            reversed_head.next = prev #1.next 뒤집은 거
        else :
            root = prev #처음에 뒤집은 경우
        
        reversed_tail.next = node #2 뒤에 역순까지 진행한 후의 node를 붙여준다.
        
        return root