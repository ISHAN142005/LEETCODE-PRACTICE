class Solution(object):
    def countDigits(self, num):
        count=0
        org=num
        
        while num>0:
            last=num%10
            num=num//10
            if(org%last==0):
                count+=1
        return count
        