# https://leetcode.com/problems/counting-bits/
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


# First Solution
# Yeah , Just noticed that I should be doing it like a Boss , without using inbuild count functions LOL !


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        my_list = []
        self.num = num
        for i in xrange(self.num+1):
            my_list.append(bin(i)[2:].count('1'))
        return my_list


# Second Solution
# Hope this is more BOSS , since I have my own count function now - I still think there might be some bit manipulation trick here
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        my_list = []
        self.num = num
        for i in xrange(self.num+1):
            my_list.append(self.my_count(bin(i),1))
        return my_list


    def my_count(self,number,search_char):
        self.count = 0
        self.number = str(number)
        self.search_char = str(search_char)
        for i in xrange(len(self.number)):
            #print "search_character = ",self.search_char
            #print self.number[i]
            if self.number[i] == self.search_char:
                self.count = self.count + 1
            else:
                continue
        return self.count

my_solution = Solution()
print my_solution.countBits(5)
#print my_solution.my_count('11111',1)
