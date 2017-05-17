'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
import pdb


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"])
        set2 = set(["a", "s", "d", "f", "g", "h", "j", "k", "l"])
        set3 = set(["z", "x", "c", "v", "b", "n", "m"])
        sul = []
        for word in words:
            if len(word) < 2:
                sul.append(word)
            elif word[1].lower() in set1:
                if self.isinset(word, set1):
                    sul.append(word)
            elif word[1].lower() in set2:
                if self.isinset(word, set2):
                    sul.append(word)
            elif word[1].lower() in set3:
                if self.isinset(word, set3):
                    sul.append(word)
        return sul

    def isinset(self, word, setnumber):
        pdb.set_trace()
        for char in word:
            if char.lower() not in setnumber:
                return False
        return True


m = Solution()
m.findWords(["Hello","Alaska","Dad","Peace"])


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1=set("qwertyuiop")
        s2=set("asdfghjkl")
        s3=set("zxcvbnm")
        sets=[set(word.lower()) for word in words]
        i=0
        ret=[]
        for sset in sets:
            if sset.issubset(s1) or sset.issubset(s2) or sset.issubset(s3):
              ret.append(words[i])
            i+=1
        return ret
