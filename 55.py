def findKthLargest(self,num,k):
    num.sort() #정렬하고
    return nums[-k] #k번째로 큰 값을 호출해준다.