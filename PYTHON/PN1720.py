class Solution(object):
    def decode(self, encoded, first):
        original=[first]
        for num in encoded:
            temp=original[-1]^num
            original.append(temp)
        return original
       