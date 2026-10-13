class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #validate each string in the window as long as the char is unique
        #run through all chars and add to set, if char in set, move left pointer up and remove char from set, need a while loop for removing since it may take multiple attempts
        #consider string "abcdc" string valid abcd then second c comes in
        #needs to then be bcdc -> cdc -> dc till valid again

        seen = set()
        l = 0
        r = 0
        maxLen = 0
        for c in s:
            while c in seen:
                #need to remove c from seen and move left pointer that marks window
                seen.remove(s[l])
                l += 1
            seen.add(c)            
            maxLen = max(maxLen, r-l + 1)
            r += 1
        return maxLen
        



                
        