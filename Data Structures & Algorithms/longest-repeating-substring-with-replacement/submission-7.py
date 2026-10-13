class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #need to find most common character
        #maybe store a map {char : count}
        #if count of any variable that isnt the most common is greater than k 
        #move window
        count = {}
        res = 0
        l = 0
        #sliding window has a consistent growing r pointer
        for r in range(len(s)):
            #count increment by adding one to current val, if not there start at 0
            count[s[r]] = 1 + count.get(s[r], 0)

            #check while the length of the windows - max occuring number in hashmap count
            #is > number allowed to replace, decrement window and count
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                #move l boundary up
                l += 1
            res = max(res, (r - l + 1))
        return res