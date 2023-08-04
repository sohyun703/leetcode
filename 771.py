class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        result= {}
        count =0
        
        for char in stones:
            if char not in result:
                result[char] =1
            else:
                result[char]+=1
        
        for char in jewels:
            if char in result:
                count+= result[char]
        
        return count