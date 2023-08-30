class Solution(object):
    def combinationSum(self, candidates, target):
        result =[]
        
        def dfs(csum, index, path):
            if csum <0:
                return
            
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], path + [candidates[i]])
                
        dfs(target,0,[])
    
        return result
            
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """