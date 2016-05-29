class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n!=1 and n not in lookup:
            n = map(int,str(n))
            n = sum([i*i for i in n])
            lookup[n] = True
        return n==1

my_solution = Solution()
print my_solution.isHappy(19)
