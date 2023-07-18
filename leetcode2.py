# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        node,prev= head,None
        while node:
            next,node.next = node.next,prev
            prev,node = node,next
        return prev
    
    #연결리스트 리스트로 전환        
    def toList(self,node): 
        List =[]
        if node :
            while node is not None:
                List.append(node.val)
                node= node.next
        return List
    
    #리스트 연결리스트로 전환
    def toReversedLinked(self,List):
        if len(List)>0:
           prev = None
           for n in List:
               node = ListNode(n)
               node.next = prev
               prev = node
        
        return prev
            
            
    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        #리스트를 문자열로 변환 -> 다시 정수로 변환하여 덧셈 과정 진행 이후 문자열로 변환해서 이를 연결리스트로 만들어준다. 
        resultStr = int (''.join(str(e) for e in a))+ \
                    int (''.join(str(e) for e in b))

        return self.toReversedLinked(str(resultStr))