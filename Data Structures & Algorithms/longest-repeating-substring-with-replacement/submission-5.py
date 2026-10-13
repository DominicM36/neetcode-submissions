class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #array storing counts of all values
        res,maxF,l = 0,0,0

        for r in range(len(s)): #go through string to update count
            #update count, should only track count within sliding window
            count[s[r]] = 1 + count.get(s[r],0)
            maxF = max(maxF, count[s[r]])
            while(r - l + 1) - maxF > k:
                #window is invalid move left:
                count[s[l]] -= 1
                l+=1
            #result = max valid window
            res = max(res, r - l + 1)

        return res
        