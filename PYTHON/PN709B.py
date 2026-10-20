class Solution(object):
    def toLowerCase(self, s):
        ans=""
        for char in s:
            if 'A' <= char <= 'Z':
                temp=ord(char)+32
                ans+=chr(temp)
            else:
                ans+=char
        return ans
        