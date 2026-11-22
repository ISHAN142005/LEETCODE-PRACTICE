class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        x=len(nums)//2
        return nums[x]

        