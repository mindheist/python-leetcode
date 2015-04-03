# https://leetcode.com/problems/compare-version-numbers/

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37

# Solution
# ========

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
    	v1,v2 = version1.split(".") , version2.split(".")
    	if len(v1) > len(v2):
    		diff = len(v1) - len(v2)
    		for i in range(diff):
    			v2.append("0")
    	elif len(v2) > len(v1):
    		diff = len(v2) - len(v1)
    		for i in range(diff):
    			v1.append("0")

    	i = 0
    	while i < max(len(v1),len(v2)):
    		if int(v1[i]) > int(v2[i]):
    			return 1
    		elif int(v2[i]) > int(v1[i]):
    			return -1
    		else:
    			i+=1
    	return 0

my_solution = Solution()

print "Test # 1"
print my_solution.compareVersion("12.2.3.4.5","12.1")
print "Test # 2"
print my_solution.compareVersion("01","1")