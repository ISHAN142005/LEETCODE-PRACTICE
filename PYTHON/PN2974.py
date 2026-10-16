class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        ans=[]
        for i in range(0,len(nums),2):
            alice=nums[i]
            bob=nums[i+1]
            ans.append(bob)
            ans.append(alice)
        return ans
       