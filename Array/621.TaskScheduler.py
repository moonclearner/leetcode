# -*- coding: utf-8 -*-
"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

n 代表n个间隔中，不能有相同的元素，不然有idle补全
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for i in tasks:
            count[ord(i) - ord('A')] += 1
        Maxfreq = max(count)
        Maxfreqnums = count.count(Maxfreq)
        """
        count = sorted(count)
        Maxfreqnums = 0
        Maxfreq = count[-1]
        for i in count:
            if i == Maxfreq:
                Maxfreqnums += 1
        """
        return max(len(tasks), (Maxfreq - 1) * (n + 1) + Maxfreqnums)

"""
public class Solution {
    public int leastInterval(char[] tasks, int n) {

        int[] c = new int[26];
        for(char t : tasks){
            c[t - 'A']++;
        }
        Arrays.sort(c);
        int i = 25;
        while(i >= 0 && c[i] == c[25]) i--;

        return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);
    }
}

 A -> B -> idle |  A -> B -> idle | A -> B.

25 - i 等于最大频率的数量

for the last line (c[25] - 1) * (n + 1) + 25 - i:

c[25]-1: we have totally "c[25]" frames,
*(n+1): the length of each frame, each of the first c[25]-1 frames must have a length of "n+1"
+25-i: count for the most frequent letters, it is the length of the last frame

ACCCEEE 2

3 identical chunks "CE", "CE CE CE" <-- this is a frame
Begin to insert 'A' --> "CEACE CE" <-- result is (c[25] - 1) * (n + 1) + 25 -i = 2 * 3 + 2 = 8
"""

m = Solution()
print m.leastInterval(['A','A','A','B','B','B'], 2)
