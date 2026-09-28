class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=0
        org=x

        while x>0:
            num=x%10
            temp=(temp*10)+num
            x=x//10
        return org==temp
        
        

        