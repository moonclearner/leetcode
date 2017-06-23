'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
    pic:https://leetcode.com/static/images/problemset/island.png
'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == 1:
                    print (x, y)
                    result = result + self.countAdjacent(x, y, grid)
        return result

    def countAdjacent(self, x, y, grid):
        sums = 4
        adjacentCoordinate = (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)
        print adjacentCoordinate
        for x, y in adjacentCoordinate:
            if len(grid) - 1 >= x >= 0 and len(grid[0]) - 1 >= y >= 0 and grid[x][y] == 1:
                sums -= 1
                print (x, y)
        print sums
        return sums


m = Solution()
print m.islandPerimeter([[1,0]])
