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

