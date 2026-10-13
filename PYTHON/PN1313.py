class Solution(object):
    def decompressRLElist(self, nums):
        ans=[]
        for i in range(0,len(nums),2):
            number=nums[i+1]
            repeat=nums[i]
            for j in range(repeat):
                ans.append(number)
        return ans

        
        