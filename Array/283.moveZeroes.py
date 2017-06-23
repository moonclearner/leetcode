"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        ans = filter(lambda x:x != 0, nums)
        ans.extend([0 for i in range(count)])
        # 注意a = ans.extend() 返回的不是合并的列表，变的结果是ans
        return ans

    def moveZeroes2(self, nums):
        flag = 0
        for i in nums:
            if i != 0:
                nums[flag] = i
                flag += 1
        while flag < len(nums):
            nums[flag] = 0
            flag += 1

    def moveZeroes3(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
