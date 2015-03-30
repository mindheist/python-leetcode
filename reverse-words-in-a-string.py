class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # Step 1 : split the given string into a list of words - with " " as the seperator
        s = s.split(" ")
        # Step 2 : filter out the white spaces in the list and reverse the list
        s = [element for element in s if element != ''][::-1]
        # Step 3 : join them and return 
        return ' '.join(s)