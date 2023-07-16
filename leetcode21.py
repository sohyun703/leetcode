


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result =[]
        
        node = list1


#첫번째 연결 리스트 리스트로 변환
        while node is not None:
            result.append(node.val)
            node =node.next
        
        node2 = list2
        

#두번째 연결 리스트 리스트로 변환
        while node2 is not None:
            result.append(node2.val)
            node2= node2.next
        
        #리스트 정렬
        result.sort()
       
       #리스트에 들은 것이 있다면 
        if len(result)>0:
            head = ListNode()
            head.val = result[0]
            current =head

            for i in range(1,len(result)):
                node = ListNode()
                node.val = result[i]
                current.next =node
                current = current.next


        else : 
            return None

        return head
