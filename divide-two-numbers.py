class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # totally the wrong way to be solving this , use bit manipulation for faaster results
        # http://stackoverflow.com/questions/5284898/implement-division-with-bit-wise-operator

        if divisor == 0:
            return -1
        elif divisor > dividend :
            return dividend
        elif divisor == 1:
            return dividend
        elif dividend > divisor:
            quotient = 0
            remainder = dividend
            while remainder > divisor :
                remainder = remainder - divisor
                quotient +=1
            return quotient
        else:
            return 1

my_solution = Solution()
print my_solution.divide(214743558,2)
# print my_solution.divide(2500,7)
# print my_solution.divide(0,7)
# print my_solution.divide(7,0)
# print my_solution.divide(42121,1)
