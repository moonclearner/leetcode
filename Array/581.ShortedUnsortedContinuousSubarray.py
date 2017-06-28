"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = -1
        right = -2
        minnum = nums[length - 1]
        maxnum = nums[0]
        for i in range(1, length):
            maxnum = max(maxnum, nums[i])
            minnum = min(minnum, nums[length - 1 - i])
            if nums[i] < maxnum:
                right = i
            if nums[length - 1 - i] > minnum:
                left = length - 1 - i
        return right - left + 1
