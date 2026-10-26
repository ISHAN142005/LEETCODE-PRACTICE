class Solution(object):
    def countPrefixes(self, words, s):
        count=0
        for x in words:
            if s.startswith(x):
                count+=1
        return count
        