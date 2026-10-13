class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on the start key
        intervals.sort(key=lambda x:x[0])

        outputs=[intervals[0]]

        for start,end in intervals:
            
            #second index of lasst added item to output
            prevEnd = outputs[-1][1]
            if prevEnd >= start:
                outputs[-1][1] = max(prevEnd, end)
            else:
                outputs.append([start, end])
        return outputs
        