"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1, i, -1):
                if target - numbers[i] == numbers[j]:
                    return [i, j]

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, len(numbers) - 1
        while head < tail:
            if numbers[head] + numbers[tail] == target:
                return [head + 1, tail + 1]
            elif numbers[head] + numbers[tail] < target:
                head += 1
            elif numbers[head] + numbers[tail] > target:
                tail -= 1

        # dictionary
        def twoSum2(self, numbers, target):
            dic = {}
            for i, num in enumerate(numbers):
                if target - num in dic:
                    return [dic[target - num] + 1, i + 1]
                dic[num] = i

        # binary search
        def twoSum(self, numbers, target):
            for i in xrange(len(numbers)):
                l, r = i + 1, len(numbers) - 1
                tmp = target - numbers[i]
                while l <= r:
                    mid = l + (r - l) // 2
                    if numbers[mid] == tmp:
                        return [i + 1, mid + 1]
                    elif numbers[mid] < tmp:
                        l = mid + 1
                    else:
                        r = mid - 1
