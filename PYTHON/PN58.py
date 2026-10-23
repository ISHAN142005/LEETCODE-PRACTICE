class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        last= words[-1]
        return len(last)