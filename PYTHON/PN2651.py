class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        result= arrivalTime+delayedTime
        if result==24:
            return 0
        elif result>24:
            return result%24
        else:
            return result

     