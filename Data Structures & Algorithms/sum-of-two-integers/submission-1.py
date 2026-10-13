class Solution:
    def getSum(self, a: int, b: int) -> int:
        #carry = a & b
        #add = a ^ b (XOR)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            #how to do addition with bit shifting
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a^mask)