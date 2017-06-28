"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # error 使用位操作
        # 0 ^ 1 = 1
        # 1 ^ 2 = 3
        # 3 ^ 3 = 0
        ans = 0
        chechlist = []
        countzero = 0
        for i in nums:
            if i == 0:
                countzero += 1
                if countzero > 1:
                    return True
            else:
                ans = ans ^ i
                if ans in chechlist:
                    return True
                chechlist.append(ans)
        return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
