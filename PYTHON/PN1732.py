class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        current = 0
        for x in gain:
            current += x
            if current > highest:
                highest = current
        return highest
