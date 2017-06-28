"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        minn = arrays[0][0]
        maxn = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            newdict = max(abs(arrays[i][0] - maxn), abs(arrays[i][-1] - minn))
            result = max(result, newdict)
            minn = min(minn, arrays[i][0])
            maxn = max(maxn, arrays[i][-1])
        return result
