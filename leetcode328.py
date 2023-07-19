# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def toList(self,head):
        if head is None:
            return
        result = []
        while head:
            result.append(head.val)
        return result
    
    def toLinked(self,result):
        if len(result)==0:
            return
        
        root =curr = ListNode(result[0])
        
        for i in range(1,len(result)):
            new = ListNode(result[i])
            curr.next = new
            curr = curr.next
        
        return root
    def OddEven(self,result):
        if len(result)==0:
            return
        
        OddList = sorted(result, key = lambda x : x/2==1)
        return OddList
    def oddEvenList(self, head):
        if head is None:
            return
        
        #연결리스트 -> 리스트
        
        ListHead = self.toList(head)
        
        #리스트 홀짝 분류 정렬
        
        OddList = self.OddEven(ListHead)
        
        #리스트 -> 연결리스트
        
        LinkOdd = self.toLinked(OddList)
        return LinkOdd
        
    #두번째로 푼 방법 -> memory 어쩌고
    def solution_new(self,head):
        root1=cur1 = ListNode(None)
        root2=cur2 = ListNode(None)
        
        cnt =1
        while head:
            if cnt/2 ==1: #홀수 노드
                new1 = ListNode(head.val)
                cur1.next = new1
                cur1 = cur1.next 
                cnt +=1
            else :
                new2 = ListNode(head.val)
                cur2.next = new2
                cur2 = cur2.next 
                cnt +=1 
        
        #root1의 꼬리와 root2의 끝 연결
        
        tail = cur1 
        while tail:
            tail = tail.next
        
        #연결
        tail.next = root2.next

        return root1.next
    def real(head):
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even  and even.next:
            odd.next = odd.next.next
            even = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even.head
        return
    def oddEvenList(head):
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even  and even.next:
            odd.next = even.next
            even.next= odd.next
            odd = odd.next
            even = even.next
        odd.next =even_head
        return head
    
    ##TimeOut