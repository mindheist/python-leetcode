# This solution passes on about 302/501 tests - the problem is with ".".

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_0 = self.get_rows(board,0)
        truth_string = []


        for i in xrange(9):
            if row_0[i] != '.':
                if self.get_columns(board,i).count(row_0[i]) < 2:
                     truth_string.insert(i,1)
                else:
                    return False
            else:
                continue

        return True

    def IsInteger(self,char):
        if char == '.':
            return False
        else:
            return True

    def print_board(self,board):
        #this is to print the board in human readable form
        for i in xrange(9):
            print self.get_rows(board,i)

    def get_rows(self,board,row_number):
        self.row_number = row_number
        self.board = board
        return self.board[row_number]

    def get_columns(self,board,column_number):
        # given a board and n from 1 to 9 , this gives columns
        self.board = board
        self.column_number = column_number
        if self.column_number > 9:
            return "Columns numbers have to be less or equal to 9"
        else:
            column_string = ""
            for i in xrange(len(self.board)-1):
                #print board[i][column_number]
                column_string = column_string + board[i][column_number]
            return column_string

my_solution = Solution()
print my_solution.isValidSudoku([".........","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])

# print my_solution.isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])
#print my_solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
