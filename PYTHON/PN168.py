class Solution(object):
    def convertToTitle(self, columnNumber):
        result=""
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            new_alpha=chr(rem+65)
            result=new_alpha+result
            columnNumber=columnNumber//26
        return result

       