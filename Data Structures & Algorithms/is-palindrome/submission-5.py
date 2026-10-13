class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for i in range(len(s)):
            if s[i].isalnum():
                newstr += s[i].lower()
        l,r = 0, len(newstr) - 1
        while l < r:
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1


        return True

        