class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            lettersS[s[i]] = lettersS.get(s[i], 0) + 1
        for i in range(len(t)):
            if t[i] in lettersS:
                lettersS[t[i]] = lettersS.get(t[i], 0) - 1
            else:
                return False
        for i in range(len(s)):
            if lettersS.get(s[i]) != 0:
                return False
        return True           