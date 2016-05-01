# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# solution explanation : http://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.mainStack) == 0:

            self.mainStack.append(x)
            self.minStack.append(x)
        else:
            self.mainStack.append(x)
            y = self.minStack[len(self.minStack)-1]
            if x < y:
                self.minStack.append(x)
            else:
                self.minStack.append(y)

    def pop(self):
        """
        :rtype: void
        """
        self.mainStack.pop()
        self.minStack.pop()


    def top(self):
        """
        :rtype: int
        """
        #print len(self.mainStack)
        # print self.minStack

        return self.mainStack[len(self.mainStack)-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[len(self.minStack)-1]


    def print_stack(self):
        print "minstack=" , self.minStack
        print "mainStack" , self.mainStack
        print "=========================="

my_minstack = MinStack()
my_minstack.print_stack()
my_minstack.push(-2)
my_minstack.print_stack()
print my_minstack.top()
my_minstack.print_stack()
# my_minstack.push(6)
# my_minstack.push(15)
# my_minstack.push(56)
# my_minstack.print_stack()
# my_minstack.push(1)
# my_minstack.print_stack()
# my_minstack.push(0)
# my_minstack.print_stack()
# my_minstack.push(10)
# my_minstack.print_stack()
# my_minstack.pop()
# my_minstack.print_stack()
# my_minstack.pop()
# my_minstack.print_stack()
# my_minstack.push(80)
# my_minstack.print_stack()

#print my_minstack.getMin()
