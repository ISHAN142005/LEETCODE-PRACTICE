class Solution(object):
    def balancedStringSplit(self, s):
        total = 0
        balance = 0

        for char in s:
            if char == "L":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                total+= 1

        return total