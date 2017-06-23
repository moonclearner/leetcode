'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max 0x0111111111111111111111111111111
        MAX = 0x7FFFFFFF
        # 32 bits interger min 0x1000000000000000000000000000000
        MIN = 0x80000000
        # mask to get last 32 bits 0x11111111111111111111111111111
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


def getsum(a, b):
    return a if b == 0 else getsum(a ^ b, (a & b) << 1)
