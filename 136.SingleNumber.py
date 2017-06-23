'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x, y in Counter(nums).items():
            if y == 1:
                return x

    def singleNumber2(self, nums):
        # ^ not same = 1 negative positive
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
            print result, nums[i]
        return result


m = Solution()
print m.singleNumber2([4, 3, 2, 2, 5, 3, 4])

