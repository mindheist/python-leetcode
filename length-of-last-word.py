# Given a string s consists of upper/lower-case alphabets and empty space characters return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        string_list = s.split(' ')
        return len(string_list[len(string_list) - 1])