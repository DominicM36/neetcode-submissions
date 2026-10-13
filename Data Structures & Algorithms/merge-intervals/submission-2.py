class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        #intervals are sorted, need to iterate through intervals and check to see if the interval is included or not

        output = [intervals[0]]
        #added start already
        for start,end in intervals[1:]:
            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(prevEnd, end)
            else:
                output.append([start, end])
        return output

        