import string 
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
		length , return_val = len(str(s)) , 0
		for i in range(length):
			#print ord(s[i])
			return_val = return_val + (ord(s[i]) - 64 ) * pow(26,length - i - 1)
		return return_val

	    # A  -- if length == 1 ; then return ord(str[0]) - 64   --> length 1 
	    # AA -- if length == 2 ; then return ( 26 * (ord(str[0]) - 64 ) +  ord(str[1]) - 64 --> length 2
		# AAA - if length == 3 ; then return ( 26*26  * (ord(str[0]) - 64 ) + 26 * (ord(str[1])-64) + ord(str[2]) - 64
		
		
		# previously tried implementing a look-up dictionary myself to map A : 1 , B:2 etc.,
		# this is available as a built in function ord("A")
		# Also took a while in finding out the pattern (