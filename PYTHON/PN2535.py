class Solution(object):
    def differenceOfSum(self, nums):
        digit_sum=0
        element_sum=0

        for i in nums:
            if i>=10:
                while i>0:
                    temp=i%10
                    digit_sum+=temp
                    i//=10
            else:
                digit_sum+=i
        
        for i in nums:
            element_sum+=i
        
        final_diff=element_sum-digit_sum
        if final_diff<0:
            return final_diff*-1
        return final_diff


               
         
    