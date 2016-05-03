from collections import Counter
class Solution:
    def return_uniquewords(self):
        f = open("two-sum.py",'r')
        self.my_counter = Counter()
        for line in f:
            line = line.strip().split()
            #print line
            for words in line:
                self.my_counter[words] +=1
        f.close()
        return self.my_counter

my_solution = Solution()
print my_solution.return_uniquewords()
