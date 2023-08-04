#개별 체이닝 방식
import collections

class ListNode():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next= next
class MyHashMap(object):

    def __init__(self):
        self.size= 1000
        self.table= collections.defaultdict(ListNode)

    def put(self, key : int , value : int):
        index = key %self.size
        
        #인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return
        
        #인덱스에 노드가 존재하는 경우
        p  = self.table[index] 
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            
            p = p.next
        p.next =ListNode(key,value) 
              
        
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key:int):
        index = key%self.size
        if self.table[index].value is None:
            return -1
        
        #노드가 존재할 때
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

        
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key : int):
        index= key&self.size
        if self.table[index].value is None:
            return
        
        #인덱스의 첫번째 노드인 경우
        
        p = self.table[index]
        if p.key == key:
            self.table[index]= ListNode() if p.next is None else p.next
            return
        """
        :type key: int
        :rtype: None
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)