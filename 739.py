class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = []
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i] >temperatures[stack[-1]]: #stack이 비어 있지 않고, 현재 온도가 stack의 가장 마지막 기온 보다 높을 때
                prev_index= stack.pop() #stack의 마지막 인덱스 제거
                result[prev_index] = i- prev_index
            
            stack.append(i)
            result.append(0) #결과 리스트 추가 ㄱㄱ
                
            
        
        return result
    
    
    
    
    
    
    
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """