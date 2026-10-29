class Solution(object):
    def isPalindrome(self, s):
        rev=[]
        for char in s:
            if char.isalnum():
                temp=char.lower()
                rev.append(temp)
        return rev==rev[::-1]
        