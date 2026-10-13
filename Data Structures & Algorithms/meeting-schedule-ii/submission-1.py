"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort meeting rooms, space 0(1) sorted in place, speed using quicksort O(logn)
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])
        count = 0
        maxCount = 0
        #at this point startTimes and endTimes contain sorted arrays of start and end
        #need to iterate through with two pointers to check if there is overlap
        #overlap checked by if start<end increment count and store max
        startP = 0
        endP = 0

        while startP < len(intervals):
            if endTimes[endP] > startTimes[startP]:
                count = count+1
                startP += 1
            else:
                count -=1
                endP += 1
            maxCount = max(maxCount, count)

        return maxCount


