class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for i in range(len(words)):
            if words[i].startswith(pref):
                count+=1
        return count
        