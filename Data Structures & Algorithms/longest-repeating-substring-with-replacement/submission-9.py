class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #check that window length is valid
        #valid would be window length - most common char <= k
        #invalid can be seen as (r-l+1) + maxCharacter > k replaceable elements 
        charCount = {}
        res = 0
        l = 0
        maxF = 0
        
        #left starts at 0, right crawls through string
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1

            maxF = max(maxF, charCount.get(s[r]))

            while (r-l+1) - maxF > k:
                #increment left and decrement count
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res