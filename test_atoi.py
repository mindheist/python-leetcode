class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        print str
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
                    print str,len(str)
                    for i in xrange(1,len(str)):
                        if ord(str[i]) in range(48,58):
                            result = result * 10 + (ord(str[i]) - ord('0'))
                        else:
                            return self.parse_result(result,"positive")
                    return self.parse_result(result,"positive")
                elif str[0] == '-':
                    print str,len(str)
                    for i in xrange(1,len(str)):
                        if ord(str[i]) in range(48,58):
                            result = result * 10 + (ord(str[i]) - ord('0'))
                            print "i=",i,"result",result
                        else:
                            print result
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

my_solution = Solution()
#print my_solution.myAtoi('     0001')

# for i in xrange(10):
#     print my_solution.myAtoi(str(i))

# print my_solution.myAtoi(')')
# print my_solution.myAtoi('+')

#print my_solution.myAtoi('+123a23')
#print my_solution.myAtoi("2147483648")
#print my_solution.myAtoi("-2000000000000")
print my_solution.myAtoi("-2147483649")
#print my_solution.myAtoi("2147483649")
#print my_solution.myAtoi("2147483649293892")
# print my_solution.myAtoi('-1')
# print my_solution.myAtoi('-+1')



# print my_solution.myAtoi("21")
# print my_solution.myAtoi("345")
# print my_solution.myAtoi("4232")
# print my_solution.myAtoi("+21")
# print my_solution.myAtoi("-21")
