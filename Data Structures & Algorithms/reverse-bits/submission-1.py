class Solution:
    def reverseBits(self, n: int) -> int:
        rev=0
        for i in range(32):
            bit = (n >> i) % 2
            rev = rev | (bit << (31-i))
        
        return rev