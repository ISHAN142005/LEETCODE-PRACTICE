class Solution(object):
    def truncateSentence(self, s, k):
        words=s.split(" ")
        temp=" ".join(words[:k])
        return temp



        