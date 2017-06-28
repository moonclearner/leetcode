"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # because multipled by a negative make big number smaller, meanwhile seek for min and max
        if len(nums) == 0:
            return 0
        curmax = nums[0]
        curmin = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            if i < 0:
                curmax, curmin = curmin, curmax
            curmax = max(i, curmax * i)
            curmin = min(i, curmin * i)
            ans = max(ans, curmax)
        return ans
