class Solution(object):
    def reversePrefix(self, word, ch):
        tempind=word.find(ch)
        str1=word[:tempind+1][::-1]
        str2=word[tempind+1:]
        return str1+str2