import unittest
class solution:
	def reverse_divisible(self,string):
		self.string = string
		if self.string == "":
			return ""
		else:
			self.div_by_3 = []
			for i in xrange(len(self.string)-1):
				if int(self.string[i])%3==0:
					self.div_by_3.append(self.string[i])
				else:
					continue

			for i in xrange(len(self.string)):
				if int(self.string[i])%3==0:
					self.string[i] = self.div_by_3.pop() # this is not possible because strings in python are immutable
				else:
					continue
		return self.string

class TestSolution(unittest.TestCase):
	my_solution = solution()

	def test_basic_input(self):
		self.assertEqual(self.my_solution.reverse_divisible("1234567890"),"1204597863")

	# def test_empty_string(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible(""),"")
	#
	# def test_all_div_by(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("03690369"),"")
	#
	# def test_long_string(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("369036903690369036903690369036903690369"),"369036903690369036903690369036903690369")
	#
	# def test_negative_numbers(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("-34574684"),"-34574684")
	#
	# def test_zero_padding(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("000034574684"),"000034574684")
	#
	# def test_float_numbers(self):
	#
	# 	self.assertEquals(self.my_solution.reverse_divisible("3457464.36938"),"3457464.36938")
	#
	# def test_alphanumberic(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("abcddjh.#$#@%"),"abcddjh.#$#@%")
	#
	# def test_with_nothing_to_reverse(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("54217887"),"54217887")
	#
	# def test_with_leading_spaces(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("      54217887"),"      54217887")
	#
	# def test_with_spaces_on_both(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("      54217887    "),"      54217887    ")
	#
	# def test_with_zeroes_and_spaces(self):
	# 	self.assertEquals(self.my_solution.reverse_divisible("      00000054217     "),"      00000054217     ")

if __name__ == "__main__":
	unittest.main()
