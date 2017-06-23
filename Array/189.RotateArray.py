"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 将nums全部翻转，返回分成前部分翻转和后一部分翻转
        for i in range(len(nums) / 2):
            nums[i], nums[- i - 1] = nums[- i - 1], nums[i]
        print nums
        for i in range(k / 4):
            nums[i], nums[- i - 1] = nums[- i - 1], nums[i]
        print nums
        for i in range(k / 2 + 1, (len(nums) - k / 2) / 2):
            nums[i], nums[- i - 1] = nums[- i - 1], nums[i]
        print nums

    def rotate2(self, nums, k):
        n = len(nums)
        # 进行翻滚
        k = k % n
        # nums[:] = 这样才会真正的改变nums的值
        nums[:] = nums[n-k:] + nums[:n-k]

    def rotate3(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
