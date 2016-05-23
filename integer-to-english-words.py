# This passes 559/601 tests. May be I should try the divion solution! will try and finish this though later.

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num = num
        self.lookup_dictionary_0 = {0:"Zero", 1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

        self.lookup_dictionary_1 = {0:"", 1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        self.lookup_dictionary_11_19 = {10 :"Ten",11 :"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        self.lookup_dictionary_10_100 = {0:"", 10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}


        # self.lookup_dictionary_10_19 = {10:"Ten" ,11 :"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty", \
        # 60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}

        if len(str(self.num)) == 1:
            return self.lookup_dictionary_0[self.num]
        elif len(str(self.num)) == 2 :
            if self.num >= 10 and self.num < 20:
                return self.lookup_dictionary_11_19[self.num]
            elif self.num >= 20:
                int_list = map(int,str(self.num))
                if int_list[1] != 0 :
                    return self.lookup_dictionary_1[int_list[0]] + " " + self.lookup_dictionary_0[int_list[1]]
                else:
                    return self.lookup_dictionary_10_100[self.num]
            else:
                return "zero"
        elif len(str(self.num)) == 3:
            return self._three_digit_conversion(self.num)
        elif len(str(self.num)) == 4:
            int_list = map(int,str(self.num))
            last_three_digits = str(int_list[1]) + str(int_list[2]) + str(int_list[3])
            if int(last_three_digits) == 0:
                return self.lookup_dictionary_0[int_list[0]] + " Thousand"
            elif len((str(int(last_three_digits))))==1:
                return self.lookup_dictionary_0[int_list[0]] + " Thousand" + " " + self.lookup_dictionary_0[int(last_three_digits)]
            elif len((str(int(last_three_digits))))==2:
                if int(last_three_digits) in self.lookup_dictionary_11_19:
                    return self.lookup_dictionary_0[int_list[0]] + " Thousand" + " " + self.lookup_dictionary_11_19[int(last_three_digits)]
                elif int(last_three_digits) in self.lookup_dictionary_10_100:
                    return self.lookup_dictionary_0[int_list[0]] + " Thousand" + " " + self.lookup_dictionary_10_100[int(last_three_digits)]
                else:
                    return self.lookup_dictionary_0[int_list[0]] + " Thousand " + self._three_digit_conversion(last_three_digits)
            else:
                    return self.lookup_dictionary_0[int_list[0]] + " Thousand " + self._three_digit_conversion(last_three_digits)

        elif len(str(self.num)) == 5:
            try:
                int_list = map(int,str(self.num))
                first_two_digits = int(str(int_list[0]) + str(int_list[1]))
                last_three_digits = str(int_list[2]) + str(int_list[3]) + str(int_list[4])
                if int(last_three_digits) == 0 :
                    if first_two_digits in self.lookup_dictionary_11_19:
                        return self.lookup_dictionary_11_19[first_two_digits] + " Thousand"
                    elif first_two_digits in self.lookup_dictionary_10_100:
                        return self.lookup_dictionary_10_100[first_two_digits] + " Thousand"
                else:
                    if first_two_digits in self.lookup_dictionary_11_19:
                        return self.lookup_dictionary_11_19[first_two_digits] + " Thousand " + self._three_digit_conversion(last_three_digits)
                    elif first_two_digits in self.lookup_dictionary_10_100:
                        return self.lookup_dictionary_10_100[first_two_digits] + " Thousand " + self._three_digit_conversion(last_three_digits)
                    else:
                        return self.lookup_dictionary_1[int_list[0]] + " " + self.lookup_dictionary_0[int_list[1]] + " Thousand " + self._three_digit_conversion(last_three_digits)

            except KeyError:
                return "zero"
        elif len(str(self.num)) == 6:
            int_list = map(int,str(self.num))
            first_part = (str(int_list[0])+str(int_list[1])+str(int_list[2]))
            second_part = (str(int_list[3])+str(int_list[4])+str(int_list[5]))
            if second_part == "000":
                return self._three_digit_conversion(first_part) + " Thousand"
            else:
                return self._three_digit_conversion(first_part) + " Thousand " + self._three_digit_conversion(second_part)
        elif len(str(self.num)) == 7:
            int_list = map(int,str(self.num))
            first_part = int_list[0]
            second_part = (str(int_list[1])+str(int_list[2])+str(int_list[3]))
            third_part = (str(int_list[4])+str(int_list[5])+str(int_list[6]))
            if second_part == "000" and third_part == "000":
                return self.lookup_dictionary_0[first_part] + " Million"
            elif second_part == "000":
                return self.lookup_dictionary_0[first_part] + " Million " + self._three_digit_conversion(third_part)
            else:
                return self.lookup_dictionary_0[first_part] + " Million " + self._three_digit_conversion(second_part) + " Thousand " + self._three_digit_conversion(third_part)
        elif len(str(self.num)) == 10:
            int_list = map(int,str(self.num))
            first_part = int_list[0]
            second_part = (str(int_list[1])+str(int_list[2])+str(int_list[3]))
            third_part = (str(int_list[4])+str(int_list[5])+str(int_list[6]))
            four_part = (str(int_list[7])+str(int_list[8])+str(int_list[9]))
            return self.lookup_dictionary_0[first_part] + " Billion " + self._three_digit_conversion(second_part) + " Million " + self._three_digit_conversion(third_part) + " Thousand " + self._three_digit_conversion(four_part)

        else:
            return "zero"

    def _three_digit_conversion(self,three_digits):
        self.three_digits = three_digits
        int_list = map(int,str(self.three_digits))
        last_two = int(str(int_list[1])+str(int_list[2]))
        if int_list[2] ==0 and int_list[1]==0 and int_list[0]==0:
            return ""
        elif int_list[2] ==0 and int_list[1]==0 and int_list[0] !=0:
            return self.lookup_dictionary_0[int_list[0]] + " Hundred"
        elif int_list[0]==0:
            return self.lookup_dictionary_1[int_list[1]] + " "+ self.lookup_dictionary_0[int_list[2]]
        elif last_two in self.lookup_dictionary_10_100:
            return self.lookup_dictionary_0[int_list[0]] + " Hundred " + self.lookup_dictionary_10_100[last_two]
        elif last_two in self.lookup_dictionary_11_19:
            return self.lookup_dictionary_0[int_list[0]] + " Hundred " + self.lookup_dictionary_11_19[last_two]
        elif int_list[1]==0:
            return self.lookup_dictionary_0[int_list[0]] + " Hundred" + " " + self.lookup_dictionary_0[int_list[2]]
        else:
            return self.lookup_dictionary_0[int_list[0]] + " Hundred" + " " + self.lookup_dictionary_1[int_list[1]] + " "+ self.lookup_dictionary_0[int_list[2]]

my_solution = Solution()
print my_solution.numberToWords(101)
# #
# # for i in xrange(121,199):
# #     print my_solution.numberToWords(i)
