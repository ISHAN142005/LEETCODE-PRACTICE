class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        add=0
        mult=1
        while n>0:
            temp=n%10
            add+=temp
            mult*=temp
            n//=10
        return mult-add

        