'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

row == 4
4*2-2=6
1     7        13
2   6 8     12 14
3 5   9  11    15
4     10       16


9
0         10
1       9 11
2     8   12
3   7     13
4 6
5

row == 3
first line:3*2 -2 =4
second line: 4
1   5
2 4 6
3
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
''' Solution
find rule of index
2*numRows -2
2*numRows -2 -2*linenumber
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = []
        inner = []
        if numRows < 2 or len(s) < 2:
            return s
        step = numRows * 2 - 2
        # fisrt row
        ret.append(s[::step])
        # inner row
        # because next num index step - i * 2
        for i in range(1, numRows - 1):
            inner.append([s[j] + s[j + (step - i * 2)] if j + (step - i * 2) < len(s) else s[j] for j in range(i, len(s), step)])
        for i in inner:
            ret.append(''.join(i))
        # final row
        ret.append(s[numRows - 1::step])
        return ''.join(ret)


m = Solution()
print m.convert("", 1)
