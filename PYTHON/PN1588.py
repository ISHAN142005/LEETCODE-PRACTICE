class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                temp=sum(arr[i:j+1])
                total+=temp
        return total

        
        