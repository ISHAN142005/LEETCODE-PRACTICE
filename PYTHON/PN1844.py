class Solution(object):
    def replaceDigits(self, s):
        ans=list(s)
        for i in range(1,len(s),2):
            temp1=ord(ans[i-1])
            temp2=int(ans[i])
            add=temp1+temp2
            final=chr(add)
            ans[i]=final
        return "".join(ans)
        