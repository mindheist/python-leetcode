import itertools	
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
    	return_list = []
    	S = sorted(S)
    	for i in range(len(S)+1):
    		return_list.extend (list(x) for x in itertools.combinations(S,i))
    	return return_list