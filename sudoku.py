'''sudoku'''
import random

debug_sudoku = [
    [[[9, 3, 4], [8, 5, 1], [7, 6, 2]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 2], [3, 8, 9], [5, 7, 6]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[5, 1, 4], [3, 6, 8], [9, 2, 7]]]
    ]

protected_line = {
    1: [0,1,2],
    2: [0,1,2],
    3: [0,1,2],
    4: [3,4,5],
    5: [3,4,5],
    6: [3,4,5],
    7: [6,7,8],
    8: [6,7,8],
    9: [6,7,8]
}
protected_column = {
    1: [0,3,6],
    2: [0,3,6],
    3: [0,3,6],
    4: [1,4,7],
    5: [1,4,7],
    6: [1,4,7],
    7: [2,5,8],
    8: [2,5,8],
    9: [2,5,8]
}


class CreateInitialBoard:
    def __init__(self):
        self.sudoku = self.create_sudoku_board()
        self.sudoku = debug_sudoku
        self.board = OutputBoard()
        self.board.set_sudoku(self.sudoku)
        self.remove_duplicates_in_line()
        self.remove_duplicates_in_column()


    def remove_duplicates_in_line(self):
        '''finds identical numbers in the sudoku'''
        board = self.board.create_sudoku_lines().copy()
        for l,line in enumerate(self.board.create_sudoku_lines()):
            duplicate = []
            for i,item in enumerate(line):
                if item not in duplicate:
                    duplicate.append(item)
                else:
                    if i in protected_line[l+1]:
                        continue
                    else:
                        board[l][i] = 0
        for line in board:
            print(line)
        print()
    
    def remove_duplicates_in_column(self):
        '''finds identical numbers per column'''
        board = self.board.create_sudoku_lines().copy()
        for column in range(9):
            protected_values = [board[line][column] for line in protected_column[column+1]]
            print(protected_values)
            duplicate = []
            for line in range(9):
                if board[line][column] not in duplicate and column in protected_column[column+1]:
                    duplicate.append(board[line][column])
                else:
                    board[line][column] = 0
        for line in board:
            print(line)
    
    def create_protected_values(self, pos_line, pos_column, pos_box):
        '''creates a list of values that are protected from being changed'''
        protected_values = []
        for line in protected_line[pos_line]:
            for column in protected_column[pos_column]:
                protected_values.append(self.sudoku[line][column][pos_box])
        return protected_values
    



    def create_sudoku_board(self) -> list:
        '''creates a 9x9 array of empty lists'''
        sudoku_board = []
        sudoku_temp = []
        sudoku_wrong = [[1,2,3],[4,5,6],[7,8,9]]
        for i in range(1,10):
            if i in (1,5,9):
                sudoku_temp.append(self.create_sudoku_box())
            else:
                sudoku_temp.append(sudoku_wrong)
            if i % 3 == 0:
                sudoku_board.append(sudoku_temp)
                sudoku_temp = []
        return sudoku_board

    @staticmethod
    def create_sudoku_box() -> list:
        '''creates one 3x3 array of numbers between 1 and 9'''
        numbers = list(range(1,10))
        random.shuffle(numbers)
        sudoku_box = [numbers[:3],numbers[3:6],numbers[6:9]]
        return sudoku_box
    

class OutputBoard:
    def __init__(self):
        self.sudoku = []

    def set_sudoku(self, s):
        '''sets the sudoku'''
        self.sudoku = s

    def create_sudoku_lines(self) -> list:
        '''prepares a list of lists to print the sudoku'''
        sudoku_line = []
        sudoku_lines = []
        for line in self.sudoku:
            for i in range(3):
                for box in line:
                    sudoku_line.extend(box[i])
                sudoku_lines.append(sudoku_line)
                sudoku_line = []
        return sudoku_lines
    
    def print_sudoku(self):
        '''prints the sudoku'''
        lines = self.create_sudoku_lines()
        for line in lines:
            print(line)
    

su = CreateInitialBoard()