"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
杨辉三角，
                                            1
                                          1  1
                                         1  2  1
                                       1  3  3  1
                                     1  4  6  4  1
                                   1  5  10  10  5  1
                                 1  6  15  20  15  6  1
                               1  7  21  35  35  21  7  1
                             1  8  28  56  70  56  28  8  1
                          1  9  36  84  126  126  84  36  9  1
                      1  10  45  120  210  252  210  120  45  10  1
                    1  11  55  165  330  462  462  330  165  55  11  1
                 1  12  66  220  495  792  924  792  495  220  66  12  1
              1  13  78  286  715  1287  1716  1716  1287  715  286  78  13  1
        1  14  91  364  1001  2002  3003  3432  3003  2002  1001  364  91  14  1
    1  15  105  455  1365  3003  5005  6435  6435  5005  3003  1365  455  105  15  1
1  16  120  560  1820  4368  8008  11440  12870  11440  8008  4368  1820  560  120  16  1

第三个与第四个的关系 [1 2 1] [1 3 3 1]
[0 1 2 1] [1 2 1 0] 每个元素对应相加 [1 3 3 1]
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if rowIndex == 0:
            return row
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

    def getRow2(self, rowIndex):
        ans = [1]
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex + 1):
            ans = [ans[x] + ans[x + 1] for x in range(len(ans) - 1)]
            ans.insert(0, 1)
            ans.append(1)
        return ans
