class Solution(object):
    def isAcronym(self, words, s):
        acr=""
        if(len(s)!=len(words)):
            return False

        for x in words:
            temp=x[0]
            acr+=temp
        return acr==s
        
        