class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        size=len(candies)
        maximum=max(candies)
        final=[]
        for num in candies:
            temp=num
            temp+=extraCandies
            if temp>=maximum:
                final.append(True)
            final.append(False)
        return final

    

        
        