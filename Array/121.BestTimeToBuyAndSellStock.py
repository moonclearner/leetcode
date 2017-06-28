"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
4 + -2 + 3 =5
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"max subarray problem" using Kadane's Algorithm.
找到一列字符串中的子集，其中和最大
For example, for the sequence of values −2, 1, −3, 4, −1, 2, 1, −5, 4; the contiguous subarray with the largest sum is 4, −1, 2, 1, with sum 6.
https://en.wikipedia.org/wiki/Maximum_subarray_problem

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :Kadane algorithm
        max_ending_here = max_so_far = prices[0]
        for i in prices[1:]:
            max_ending_here = max(i, max_ending_here + i)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
        """
        maxcur = 0
        ans = 0
        if len(prices) == 0:
            return 0
        pre = prices[0]
        for i in prices[1:]:
            maxcur += i - pre
            maxcur = max(0, maxcur)
            ans = max(ans, maxcur)
            pre = i
        return ans
