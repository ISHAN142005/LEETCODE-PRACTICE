class Solution(object):
    def interpret(self, command):
        ans=command.replace("()","o").replace("(al)","al")
        return ans
        