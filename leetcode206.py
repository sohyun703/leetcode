# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        #1번 리스트에 다 넣고 reverse()함수를 통해 재정렬 -> 다시 연결리스트로 만들어주기

        #연결리스트 -> 리스트

        if head is None:
            return
        arr =[]
        while head is not None:
            arr.append(head.val)
            head=head.next
        #리스트를 뒤집기
        arr.reverse()

        #리스트를 연결리스트로

        if len(arr)>0:
            head_node = ListNode(arr[0])
            current = head_node

            for i in range(1,len(arr)):
                new_node = ListNode(arr[i])
                current.next = new_node
                current = current.next
            
        return head_node
