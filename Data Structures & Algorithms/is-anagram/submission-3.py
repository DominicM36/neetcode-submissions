class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {} #create a hashmap for letters in first string

        #add and remove letters from the set as they appear
        #set should be empty if valid anagram
        if len(s) != len(t):
            return False

        
        for c in s:
            lettersS[c] = lettersS.get(c, 0) + 1

        for c in t:
            if c in lettersS:
                lettersS[c] = lettersS[c] - 1
        
        for count in lettersS.values():
            if count != 0:
                return False
        return True