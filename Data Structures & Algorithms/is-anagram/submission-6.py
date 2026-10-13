class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {} #create a hashmap for letters in first string, key is letter val is count
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            lettersS[s[i]] = lettersS.get(s[i], 0) + 1
            #populate
        for i in range(len(t)):
            if t[i] in lettersS.keys():
                lettersS[t[i]] = lettersS.get(t[i], 0) - 1
            else:
                return False
        for k in lettersS.values():
            if k != 0:
                return False
        return True

            