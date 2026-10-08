class Solution(object):
    def finalValueAfterOperations(self, operations):
        final=0
        for char in operations:
            if char=='X++' or char=='++X':
                final+=1
            elif char=='X--' or char=='--X':
                final-=1
        return final
       