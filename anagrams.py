
# # Anagrams : https://leetcode.com/problems/anagrams/

# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

# Solution
# ========
# (1) list filtering : http://www.diveintopython.net/power_of_introspection/filtering_lists.html

# (2) list filering : http://www.thegeekstuff.com/2014/05/python-filter-and-list/

# (3) Collections counter : http://pymotw.com/2/collections/counter.html

# (4) python lambda : http://www.secnetix.de/olli/Python/lambda_functions.hawk

import collections
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        count = collections.Counter([''.join(sorted(str)) for str in strs])
        # (1) when using sorted() on a string, it gets sorted and becomes a list of chacters
        # (2) join them back to form a string
        # (3) counter returns a dictionary of word:count



        # print  "Count == " , count
        # print  "strs == " , strs
        # for elem in strs:
        # 	print elem,count[''.join(sorted(elem))]

        return_list = [ elem for elem in strs if count[''.join(sorted(elem))]>1]
        
        # filter the list , such that the count[elem] > 1

        return return_list
        #return filter(lambda x: count[''.join(sorted(x))] > 1, strs)

#Testing Code
#==============
# my_solution = Solution()
# strs = ['Hello','elloH','oHell','world','first','program']
# print my_solution.anagrams(strs)