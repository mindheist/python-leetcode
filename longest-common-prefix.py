# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# Reading : http://stackoverflow.com/questions/27486309/how-does-iter-and-key-in-python-max-min-function-work

# Brilliant python solution ! this could be more concise , I have kept it longer for code readability
# Hash every character (ie s[i]), if the length of the hash for that character is more than one - then break out of the loop
import unittest
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        else:
            i = 0
            length = len(min(strs,key=len))
            while i < length:
                if len({s[i] for s in strs}) !=1 :
                    break
                else:
                    i+=1
            return strs[0][:i]

class TestLCP(unittest.TestCase):
    my_solution = Solution()


if __name__ == "__main__":
    unittest.main()
