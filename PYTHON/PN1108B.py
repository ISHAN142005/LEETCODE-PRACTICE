class Solution(object):
    def defangIPaddr(self, address):
        ans=""
        for num in address:
            if num==".":
                ans+="[.]"
            else:
                ans+=num
        return ans
        