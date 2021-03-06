"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

注意 范围是[-1000, 1000]

>>> import itertools
>>> list(itertools.combinations('abc', 2))
[('a', 'b'), ('a', 'c'), ('b', 'c')]
>>> list(itertools.permutations('abc',2))
[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
>>>

"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        del nums[3:-3]
        import itertools
        return max(a * b * c for a, b, c in itertools.combinations(nums, 3))

    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = 1001
        min2 = 1002
        max1 = -1001
        max2 = -1002
        max3 = -1003
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return max(min1 * min2 * max1, max1 * max2 * max3)
