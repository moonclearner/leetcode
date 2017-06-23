"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
eg:
    [4,3,2,1]
output:
    [4,3,2,2]
eg:
    [4,3,3,9]
output:
    [4,3,4,0]
eg:
    [4,9,9,9]
output:
    [5,0,0,0]
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) -1 -i))
        return [int(i) for i in str(num + 1)]
