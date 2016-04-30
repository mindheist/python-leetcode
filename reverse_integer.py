# https://leetcode.com/problems/reverse-integer/

#Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321
#  Looks like l33tcode has this solution implemented for Java/ C , Note that
# the system max in those languages have a different range


import sys
class Solution:
    # @return an integer
    def reverse(self, x):
    	isNegative = False
    	new_sysmax = int(math.pow(2,31)-1)
    	new_sysmin = new_sysmax*-1
    	if x < 0 :
    		rev_int = int(str(abs(x))[::-1])*-1
    		if rev_int < new_sysmin:
    		    return 0
    		else:
    		    return rev_int
    	else:
    	    rev_int = int(str(abs(x))[::-1])
    	    if rev_int < new_sysmax:
    	        return rev_int
    	    else:
    	        return 0
