class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        indices={"type":0,"color":1,"name":2}
        index=indices[ruleKey]
        for item in items:
            if item[index]==ruleValue:
                count+=1
        return count
        

        
        