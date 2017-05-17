# -*- coding: utf-8 -*-
import pdb
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

example one
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

example two
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        m = 1
        if length1 == 0:
            Snums1 = 0
            m = 2
        else:
            if length1 != 1:
                if len(nums1) % 2 == 1:
                    Snums1 = float(nums1[length1 / 2]) / 2
                elif int(nums1[length1 / 2] - nums1[length1 / 2 - 1]) == 0:
                    Snums1 = nums1[length1 / 2]
                else:
                    Snums1 = (float(nums1[length1 / 2] - nums1[length1 / 2 - 1]) / 2 + nums1[length1 / 2 - 1]) / 2
            else:
                Snums1 = float(nums1[0]) / 2
        if length2 == 0:
            Snums2 = 0
            m = 2
        else:
            if length2 != 1:
                if length2 % 2 == 1:
                    Snums2 = float(nums2[length2 / 2]) / 2
                elif int(nums2[length2 / 2] - nums2[length2 / 2 - 1]) == 0:
                    Snums2 = nums2[length2 / 2]
                else:
                    Snums2 = (float(nums2[length2 / 2] - nums2[length2 / 2 - 1]) / 2 + nums2[length2 / 2 - 1]) / 2
            else:
                Snums2 = float(nums2[0]) / 2
            #  pdb.set_trace()
        return (Snums1 + Snums2) * m


#  nums1 = [1, 1]
#  nums2 = [1, 2]
#  S = Solution()
#  print S.findMedianSortedArrays(nums1, nums2)


# 该题目的意思是，将A 和
# B的数组组成一个数组，排列之后，如果总和数组是一个奇数，则去中间的数，如果总和是一个偶数，则取中间的两个数，求平均
# 题目要求O(log(m+n))的时间复杂度。这道题其实考察的是二分查找
# 每次丢去k/2+1 个数
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        s = length1 + length2
        if s % 2 == 1:
            return self.getKth(nums1, nums2, s / 2 + 1)
        else:
            # *0.5 可以避免类型转换，当数组和是一个偶数的时候是中间的两个数的平均和
            return (self.getKth(nums1, nums2, s / 2) + self.getKth(nums1, nums2, s / 2 + 1)) * 0.5

    def getKth(self, A, B, k):
        length1 = len(A)
        length2 = len(B)
        if length1 > length2:
            # 调换位置，将数组小的放在前面
            return self.getKth(B, A, k)
        if length1 == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        # 减1的原因是，序号是从0开始的
        m = k / 2 - 1
        # 为了避免m大于length1的时候
        a = min(m, length1 - 1)
        b = m
        # 每次最多可以舍去k/2个数
        if A[a] <= B[b]:
            return self.getKth(A[a + 1:], B, k - a - 1)
        else:
            return self.getKth(A, B[m + 1:], k - m - 1)


a = [1]
b = [2, 3, 4, 5, 6]
z = Solution2()
print z.findMedianSortedArrays(a, b)
