# class Solution:
#     def insertionSort(self,list):
#         self.my_list = list
#
#         for i in xrange(1,len(self.my_list)):
#             # starting one index ahead
#             currentvalue = self.my_list[i]
#             position = i
#
#             while position>0 and currentvalue > self.my_list[position-1]:
#                 # if the incoming value is less , it has to trickle down to its spot
#                 self.my_list[position] = self.my_list[position-1]
#                 position = position-1
#             self.my_list[position]=currentvalue
#             #print self.my_list
#         return self.my_list
#
# my_solution = Solution()
# print my_solution.insertionSort([9,8,7,6])
