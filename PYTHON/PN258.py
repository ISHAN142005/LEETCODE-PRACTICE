class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num>=10:
            cSum=0
            while num>0:
                last=num%10
                cSum=cSum+last
                num=num//10
            num=cSum
        return num
              
                
        
 