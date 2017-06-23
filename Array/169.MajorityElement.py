# -*- coding: utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority = nums[0]
        for i in range(len(nums)):
            if count == 0:
                count += 1
                majority = nums[i]
            elif nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority

m = Solution()
print m.majorityElement([3,3,3,3,4,6,7])
