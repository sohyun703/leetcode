#파이썬 기본 연결리스트 구조

class Node():
    def __init(self,data):
        self.data= data
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        result =[]
        current = head
        while current.next is not None:
            result.append(current.data)
            current = current.next
        
    
        while len(result) >0:
            if result.pop() == result.pop(-1):
                continue 
            else :
                return False
        return True