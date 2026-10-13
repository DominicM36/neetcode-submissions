class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #array storing counts of all values
        res = 0

        #make pointers:
        l = 0 #r will be determined by for loop

        for r in range(len(s)): #go through string to update count
            #update count, should only track count within sliding window
            count[s[r]] = 1 + count.get(s[r],0)
            #need condition to make window valid
            #while [window size] - [most occuring letter in map] > k
            while(r - l + 1) - max(count.values()) > k:
                #window is invalid move left:
                count[s[l]] -= 1
                l+=1
            #result = max valid window
            res = max(res, r - l + 1)

        return res
        