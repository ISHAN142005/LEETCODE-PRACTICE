class Solution(object):
    def missingNumber(self, nums):
        Length=len(nums)
        ExpSum=Length*(Length+1)//2
        OrgSum=sum(nums)
        return ExpSum-OrgSum