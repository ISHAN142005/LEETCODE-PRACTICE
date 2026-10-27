class Solution(object):
    def areOccurrencesEqual(self, s):
        initial=s.count(s[0])  
        for i in range(len(s)-1):
            if s.count(s[i])!=initial:
                return False
        return True
