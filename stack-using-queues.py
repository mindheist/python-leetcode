# https://leetcode.com/problems/implement-stack-using-queues/

# Implement the following operations of a stack using queues.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack)

import unittest

class Queue:
    def __init__(self):
        self.my_queue = []

    def enqueue(self,item):
        self.my_queue.insert(0,item)

    def pop(self):
        return self.my_queue.pop()

    def isempty(self):
        return len(self.my_queue)==0

    def len(self):
        return len(self.my_queue)

    def print_queue(self):
        return self.my_queue

    def top(self):
        return self.my_queue[len(self.my_queue)-1]

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_queue = Queue()
        self.temp_queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.x = x
        if self.my_queue.isempty():
            print "Empty Stacking , Adding first element"
            self.my_queue.enqueue(self.x)
        else:
            print "The stack already has",self.my_queue.len(),"elements"
            for i in range(self.my_queue.len()):
                self.temp_data = self.my_queue.pop()
                print "popping ",self.temp_data
                self.temp_queue.enqueue(self.temp_data)
            print "temp q ---> ",self.temp_queue.print_queue()
            self.my_queue.enqueue(self.x)
            print "my queue -->",self.my_queue.print_queue()

            for i in range(self.temp_queue.len()):
                self.temp_data = self.temp_queue.pop()
                self.my_queue.enqueue(self.temp_data)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.my_queue.isempty():
            print "Can Pop from Empty Stack"
        else:
            return self.my_queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.my_queue.isempty():
            return None
        else:
            return self.my_queue.top()


    def empty(self):
        """
        :rtype: bool
        """
        return self.my_queue.isempty()

    def print_stack(self):
        return self.my_queue.print_queue()

class TestStackUsingQueues(unittest.TestCase):
    my_stack = Stack()

    def test_isEmpty(self):
        self.assertTrue(self.my_stack.empty())

    def test_top(self):
        self.my_stack.push(5)
        self.assertEquals(self.my_stack.top(),5)

if __name__ == "__main__":
    unittest.main()
