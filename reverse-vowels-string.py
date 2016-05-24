# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Subscribe to see which companies asked this question

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
        else:
            vowels = ['a','e','i','o','u','A','E','I','O','U']
            vowels_in_s = []
            for i in xrange(len(s)):
                if s[i] in vowels:
                    vowels_in_s.append(s[i])
                else:
                    continue
            s = list(s)
            for i in xrange(len(s)):
                if s[i] in vowels:
                    s[i] = vowels_in_s.pop()
                else:
                    continue
            return ''.join(s)
