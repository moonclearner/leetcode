"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        currentrow = [1]
        ans = [[1]]
        if numRows == 0:
            return 0
        for i in range(numRows - 1):
            currentrow = [currentrow[x] + currentrow[x + 1]
                          for x in range(len(currentrow) - 1)]
            currentrow.insert(0, 1)
            currentrow.append(1)
            ans.append(currentrow)
        return ans


m = Solution()
print m.generate(4)


class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1] * (i + 1) for i in range(numRows)]
        print(pascal)
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascall
