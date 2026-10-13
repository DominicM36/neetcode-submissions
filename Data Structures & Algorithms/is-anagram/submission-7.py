class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {} #create a hashmap for letters in first string, key is letter val is count
        lettersT = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            lettersS[s[i]] = lettersS.get(s[i], 0) + 1
            #populate
        for i in range(len(t)):
            lettersT[t[i]] = lettersT.get(t[i], 0) + 1

        return lettersT == lettersS

            