# -*- coding: utf-8 -*-
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.calculateHamming(self.calculateBinary(x), self.calculateBinary(y))

    def calculateBinary(self, num):
        sul = []
        rem = num
        if rem < 2:
            # because reverse order
            return [rem, 0]
        while rem != 0:
            # before cal resul, append reminderreminder
            sul.append(rem % 2)
            rem = rem / 2
        #  return sul[::-1]
        return sul

    def calculateHamming(self, x, y):
        dist = 0
        print x, y
        minlen = min(len(x), len(y))
        print minlen
        for i in xrange(minlen):
            if x[i] != y[i]:
                dist += 1
        if len(x) > len(y):
            dist += sum(x[minlen:])
        else:
            dist += sum(y[minlen:])
        return dist


m = Solution()
print m.hammingDistance(0, 10)


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # ^ XOR exclusive or
        # bin inter to binary string
        # string.count("string")  count string
        return bin(x ^ y).count('1')
