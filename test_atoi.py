# TODO : Use REGEX and parse the string first .
#https://leetcode.com/problems/string-to-integer-atoi/

# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
# Subscribe to see which companies asked this question


# Note this is a really overloaded question - just because the input can be do diverse
# This also makes it a good candidate to write a bunch of test cases
import unittest
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #print str
        sys_max =  2147483647
        sys_min = -2147483649
        result = 0
        str = str.strip(" ")
        str = str.lstrip("0")
        #print str , type(str)
        #print len(str)
        if len(str) == 0:
            return 0
        elif len(str)==1:
            if ord(str[0]) not in range(48,58) :
                return 0
            else:
                return ord(str[0]) - ord('0')
        elif len(str) >1:
            #print "length greater than 1"
            if str[0] in ('+','-') and str[1] in ('+','-'):
                return 0
            else:
                if str[0] == '+':
                    #print "in here"
                    #print str,len(str)
                    for i in xrange(1,len(str)):
                        if ord(str[i]) in range(48,58):
                            result = result * 10 + (ord(str[i]) - ord('0'))
                        else:
                            return self.parse_result(result,"positive")
                    return self.parse_result(result,"positive")
                elif str[0] == '-':
                    #print str,len(str)
                    for i in xrange(1,len(str)):
                        if ord(str[i]) in range(48,58):
                            result = result * 10 + (ord(str[i]) - ord('0'))
                            #print "i=",i,"result",result
                        else:
                            #print result
                            return self.parse_result(result,"negative") * -1
                    return self.parse_result(result,"negative") * -1
                else:
                    for i in xrange(len(str)):
                        if ord(str[i]) in range(48,58):
                            result = result * 10 + (ord(str[i]) - ord('0'))
                        else:
                            return self.parse_result(result,"positive")
                    return self.parse_result(result,"positive")

    def parse_result(self,unparsed_result,sign):
        if unparsed_result > 2147483647:
            if sign  == "negative":
                return 2147483648
            else:
                return 2147483647
        else:
            return unparsed_result


class Testatoi(unittest.TestCase):
    my_solution = Solution()

    def test_basic_input_one(self):
        self.assertEqual(self.my_solution.myAtoi("42"),42)

    def test_input_zero(self):
        self.assertEqual(self.my_solution.myAtoi("0"),0)

    def test_input_with_plus_sign(self):
        self.assertEqual(self.my_solution.myAtoi("+111"),111)

    def test_input_with_negative_sign(self):
        self.assertEqual(self.my_solution.myAtoi("-10"),-10)

    def test_input_with_leading_spaces(self):
        self.assertEqual(self.my_solution.myAtoi("         200"),200)

    def test_positive_integer_with_leading_spaces(self):
        self.assertEqual(self.my_solution.myAtoi("       +200"),200)

    def test_negative_integer_with_leading_spaces(self):
        self.assertEqual(self.my_solution.myAtoi("       -200"),-200)

    def test_positive_integer_with_leading_zeros(self):
        self.assertEqual(self.my_solution.myAtoi("00000100"),100)

    def test_positive_integer_with_leading_zeros_and_spaces(self):
        self.assertEqual(self.my_solution.myAtoi("       00000100"),100)

    def test_greater_that_system_max(self):
        self.assertEqual(self.my_solution.myAtoi("2147483650"),2147483647)

    def test_exactly_system_max(self):
        self.assertEqual(self.my_solution.myAtoi("2147483647"),2147483647)

    def test_greater_than_system_min(self):
        self.assertEqual(self.my_solution.myAtoi("-2147483650"),-2147483648)

    def test_exactly_system_min(self):
        self.assertEqual(self.my_solution.myAtoi("-2147483648"),-2147483648)

    def test_really_large_positive_overflow(self):
        self.assertEqual(self.my_solution.myAtoi("2147483649293892"),2147483647)

    def test_really_large_negative_overflow(self):
        self.assertEqual(self.my_solution.myAtoi("-2000000000000"),-2147483648)

    def test_alphanumberic_input_no_sign(self):
        self.assertEqual(self.my_solution.myAtoi("123a23"),123)

    def test_alphanumberic_input_positive_sign(self):
        self.assertEqual(self.my_solution.myAtoi("+123a23"),123)

    def test_alphanumberic_input_negative_sign(self):
        self.assertEqual(self.my_solution.myAtoi("-123a23"),-123)



if __name__ == '__main__':
    unittest.main()


# print my_solution.myAtoi(')')
# print my_solution.myAtoi('+')
# print my_solution.myAtoi('-+1')
