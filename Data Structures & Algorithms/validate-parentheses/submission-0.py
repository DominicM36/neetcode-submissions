class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #map to track counterpart
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            #check if closing bracket
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False