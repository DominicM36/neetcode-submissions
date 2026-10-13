class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        #need to sort it first
        #then iterate through the sorted list
        #check first if overlap, if overlap, remove the one with the bigger end

        #save first end value
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            #not overlapping
            if start >= prevEnd:
                prevEnd = end
            else:
                ans += 1
                prevEnd = min(prevEnd, end)
        return ans