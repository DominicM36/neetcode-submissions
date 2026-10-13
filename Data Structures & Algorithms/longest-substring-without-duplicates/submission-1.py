class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #check if new char exists in set(duplicate) and move left pointer till its not true

        l = 0
        charSet = set()
        result = 0 #length of longest substring

        for r in range(len(s)): #r is index, pointer leads through loop
            #loop to check for duplicates
            while s[r] in charSet:
                charSet.remove(s[l])
                #carry rear of window up here by removing back char until r is removed
                l += 1
            charSet.add(s[r]) #add r now that we know there is no dup

            result = max(result, r-l + 1)

        return result

                
        