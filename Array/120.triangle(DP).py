"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [*2*],
    [*3*,4],
   [6,*5*,7],
  [4,*1*,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        path = triangle[-1]
        bottom = triangle[-1]
        for layer in triangle[-2::-1]:
            for index in range(len(layer)):
                path[index] = min(bottom[index], bottom[index + 1]) + layer[index]
        return path[0]
