class Solution(object):
    def leftRightDifference(self, nums):
        ans=[]
        right_sum=sum(nums)
        left_sum=0
        for num in nums:
            right_sum-=num
            temp=abs(left_sum-right_sum)
            ans.append(temp)
            left_sum+=num
        return ans
      