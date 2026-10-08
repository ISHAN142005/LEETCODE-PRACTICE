class Solution(object):
    def runningSum(self, nums):
        runsum=[]
        for i in range(len(nums)):
            if i==0:
                sum=nums[i]
                runsum.append(sum)
            else:
                sum=sum+nums[i]
                runsum.append(sum)
        return runsum
            
        
        