#https://leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


# Solution
# ========
# (1) The idea is fairly straight forward - Use a dictionary of Key:values ( in which the roman numerals are the Keys and the values are the integer equivalents

# (2) The character string will be parsed from right to left

# (3) the variable "running_value" tracks the result so far

# (4) Keep adding to the result if the romans numbers are in the increasing order

# (5) In case the onder decreases , subtract that value from the result (ie) ex: IV - while parsing from Right to Left I < V , subtract the value of I from V

class Solution:
    # @return an integer
    def romanToInt(self, s):
    	# http://en.wikipedia.org/wiki/Roman_numerals

		# I	1
		# V	5
		# X	10
		# L	50
		# C	100
		# D	500
		# M	1,000

		running_value = 0
		previous_value = 0
		romans = { 'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 ,'M':1000 }
		for i in range(len(s)-1,-1,-1):
			#print s[i]
			if romans[s[i]] < previous_value:
				running_value = running_value - romans[s[i]]
			else:
				running_value = running_value + romans[s[i]]
			previous_value = romans[s[i]]
		return running_value

my_solution = Solution()
# print "XXX =" , my_solution.romanToInt('XXX')
# print "XXXV =" , my_solution.romanToInt('XXXV')
# print "XL = " , my_solution.romanToInt('XL')
print "MCMXCVI = " , my_solution.romanToInt('MCMXCVI')
print my_solution.romanToInt('XLIX')
