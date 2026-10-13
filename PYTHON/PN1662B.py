class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        n1=[]
        n2=[]
        for c in word1:
            n1+=c
        for d in word2:
            n2+=d
        return n1==n2