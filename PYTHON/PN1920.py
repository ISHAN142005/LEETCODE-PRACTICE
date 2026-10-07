class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            temp=nums[i]

            new=nums[temp]
            ans.append(new)
        return ans
        

        