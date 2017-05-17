# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

解题思路：使用一个哈希表，记录字符的索引。例如对于字符串'zwxyabcabczbb'，当检测到第二个'a'时，由于之前已经有一个'a'了，所以应该从第一个a的下一个字符重新开始测算长度，但是要把第一个a之前的字符在哈希表中对应的值清掉，如果不清掉的话，就会误以为还存在重复的。比如检测到第二个'z'时，如果第一个'z'对应的哈希值还在，那就出错了，所以要把第一个'a'之前的字符的哈希值都重置才行。
'''
import pdb


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictl 记录每个字母的位置
        # p1 指向第一个字母的开头
        # p2 指向第二字母的开头
        dictl = {}
        p1 = 0
        p2 = 0
        maxlen = 0
        while p2 < len(s):
            # p 获取字典中，当前字母的位置，如何没有记录到字典则返回None
            p = dictl.get(s[p2], None)
            if p is None:
                #  pdb.set_trace()
                dictl[s[p2]] = p2
                p2 += 1
                # 比较以前存的最大情况和现在p2 到p1的长度，选出最大即可
                maxlen = max(maxlen, p2 - p1)
            else:
                # 将p2对应的字符删掉，p1增加一段长度
                if p1 < p2:
                    #  pdb.set_trace()
                    dictl.pop(s[p1])
                    p1 += 1
        return maxlen


m = Solution()
print m.lengthOfLongestSubstring("dvdf")
