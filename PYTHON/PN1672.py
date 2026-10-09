class Solution(object):
    def maximumWealth(self, accounts):
        wealth=0
        for customers in accounts:
            if sum(customers)>wealth:
                wealth=sum(customers)
        return wealth


       
        