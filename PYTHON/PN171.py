class Solution(object):
    def titleToNumber(self, columnTitle):
        total=0
        for char in columnTitle:
            temp=ord(char)-64
            total=(total*26)+temp
        return total

        