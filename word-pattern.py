class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()):
            return False
        else:
            my_dict = {}
            for i in xrange(len(pattern)):
                if pattern[i] not in my_dict:
                    if str.split()[i] in my_dict.values():
                        return False
                    else:
                        my_dict[pattern[i]] = str.split()[i]
                elif pattern[i] in my_dict:
                    print pattern[i],my_dict[pattern[i]],str.split()[i]
                    if my_dict[pattern[i]] != str.split()[i]:
                        return False
                    else:
                        my_dict[pattern[i]] = str.split()[i]
            return True


my_solution = Solution()
print my_solution.wordPattern("abba","dog cat cat sheep")
print my_solution.wordPattern("abba","dog cat cat dog")
print my_solution.wordPattern("abba","dog dog dog dog")
