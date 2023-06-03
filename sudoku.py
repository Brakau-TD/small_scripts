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

# coordinates are [line][column]
# on a 2D array
protected_coordinates = [
    [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
    [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
]

class CreateInitialBoard:
    def __init__(self):
        self.sudoku = self.create_sudoku_board()
        self.sudoku = debug_sudoku
        self.board = OutputBoard()
        self.board.set_sudoku(self.sudoku)
        self.clean_up_initial_lines()
        print(self.sudoku)


    def clean_up_initial_lines(self):
        '''finds identical numbers in the sudoku and replaces them with 0'''
        board = self.board.create_sudoku_lines().copy()
        for l,line in enumerate(self.board.create_sudoku_lines()):
            duplicate = []
            for i,item in enumerate(line):
                if item not in duplicate and self.check_if_protected([l,i]):
                    duplicate.append(item)
                elif item not in duplicate and self.check_if_protected([l,i]) == False:
                    duplicate.append(item)
                elif item in duplicate and self.check_if_protected([l,i]) == True:
                    location = line.index(item)
                    board[l][location] = 0 if [l,location] != [l,i] else None
                else:
                    board[l][i] = 0
        self.sudoku = board
        print()
    
    def clean_up_initial_columns(self):
        '''finds duplicates in the columns and replaces them with 0'''
        board = self.board.create_sudoku_lines().copy()
        for c,column in enumerate(board):
            column_duplicates = []
            pass
            for line in range(0,9):
                pass
    
    def check_if_protected(self, coordinate: list):
        '''finds identical numbers per column'''
        board = self.board.create_sudoku_lines().copy()
        for line in protected_coordinates:
            if coordinate in line:
                return True
        return False
    

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