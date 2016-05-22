# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

import unittest
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.auxillary_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        if len(self.main_stack) == 0 :
            self.main_stack.append(x)
        else:
            for i in  xrange(len(self.main_stack)):
                self.temp_data = self.main_stack.pop()
                self.auxillary_stack.append(self.temp_data)

            self.main_stack.append(x)

            for i in xrange(len(self.auxillary_stack)):
                self.temp_data = self.auxillary_stack.pop()
                self.main_stack.append(self.temp_data)

    def pop(self):
        """
        :rtype: nothing
        """
        return self.main_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.main_stack[len(self.main_stack)-1]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.main_stack)==0:
            return True
        return False
        #return self.main_stack[len(self.main_stack)-1] ==0

class TestQueueUsingStacks(unittest.TestCase):
    my_queue = Queue()

    def test_empty_function(self):
        self.assertTrue(self.my_queue.empty())

    def test_peek_function(self):
        self.my_queue.push(6)
        self.assertEquals(self.my_queue.peek(),6)

    def test_pop_function(self):
        self.assertEquals(self.my_queue.pop(),6)



if __name__ == "__main__":
    unittest.main()
