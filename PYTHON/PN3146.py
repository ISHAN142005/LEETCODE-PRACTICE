class Solution(object):
    def findPermutationDifference(self, s, t):
        total=0
        for i in range(len(s)):
            temp=s[i]
            index=t.index(temp)
            temp_add=abs(i-index)
            total+=temp_add
        return total

        