class Solution(object):
    def alternateDigitSum(self, n):
        digit_string=str(n)
        total=0
        sign=1
        for char in digit_string:
            temp=int(char)*sign
            total+=temp
            sign*=-1
        return total

        