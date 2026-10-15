class Solution(object):
    def sumOfSquares(self, nums):
        total=0
        n=len(nums)
        for i in range(n):
            temp=i+1
            if(n%temp==0):
                total+=nums[i]*nums[i]
        return total
                






        
        