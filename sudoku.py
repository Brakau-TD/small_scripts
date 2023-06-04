'''sudoku'''
import random
from collections import Counter


debug_sudoku = [
    [[[8, 1, 5], [6, 2, 7], [9, 3, 4]], [[3, 9, 7], [2, 4, 8], [1, 5, 6]], [[5, 7, 6], [4, 8, 9], [1, 3, 2]]],
    [[[6, 1, 4], [9, 8, 5], [2, 7, 3]], [[4, 1, 7], [8, 3, 5], [2, 9, 6]], [[7, 2, 3], [5, 4, 8], [9, 6, 1]]],
    [[[3, 5, 4], [7, 6, 1], [2, 9, 8]], [[6, 1, 2], [5, 7, 3], [8, 4, 9]], [[9, 4, 5], [7, 8, 6], [2, 3, 1]]]
    ]

# coordinates are [line][column]
# on a 2D array
protected_coordinates = [
    [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
    [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
]


class CreateInitialBoard:
    def __init__(self):
        self.possible_numbers = list(range(1,10))
        self.board = OutputBoard()
        self.sudoku = self.board.create_sudoku_board()
        self.sudoku = debug_sudoku
        sudoku_temp = self.board.create_sudoku_lines(self.sudoku)
        sudoku_temp = self.clean_up_initial_sudoku(sudoku_temp)
        sudoku_temp = self.board.create_sudoku_columns(sudoku_temp)
        sudoku_temp = self.clean_up_initial_sudoku(sudoku_temp)
        sudoku = self.board.create_sudoku_columns(sudoku_temp)

        self.board.print_sudoku(sudoku, "Cleaned Sudoku")
        sudoku_temp = self.fill_blanks(sudoku)
        self.board.print_sudoku(sudoku_temp, "Filled Sudoku")
        sudoku_temp = self.nine_boxes(sudoku_temp)
        self.find_duplicate_in_box(sudoku_temp)



    def clean_up_initial_sudoku(self, my_sudoku: list):
        '''finds identical numbers in the sudoku and replaces them with 0'''
        board = my_sudoku.copy()
        for l,line in enumerate(my_sudoku):
            line_duplicate = []
            for i,item in enumerate(line):
                if item not in line_duplicate and self.check_if_protected([l,i]):
                    line_duplicate.append(item)
                elif item not in line_duplicate and self.check_if_protected([l,i]) == False:
                    line_duplicate.append(item)
                elif item in line_duplicate and self.check_if_protected([l,i]) == True:
                    location = line.index(item)
                    board[l][location] = 0 if [l,location] != [l,i] else None
                else:
                    board[l][i] = 0
        return board
    
    def fill_blanks(self, my_sudoku: list):
        new_sudoku = my_sudoku.copy()
        for l, line in enumerate(my_sudoku):
            for i,item in enumerate(line):
                if item == 0:
                    possible_numbers = self.get_possible_numbers_in_line(line)
                    final_choices = self.check_possible_numbers_in_column(possible_numbers, my_sudoku, i)
                    number = random.choice(final_choices) if len(final_choices) > 0 else 0
                    print(f'Choices: {final_choices}. I chose: {number}')
                    new_sudoku[l][i] = number
        return new_sudoku

    
    def get_possible_numbers_in_line(self, line) -> list:
        '''returns a list of possible numbers for a blank space (line-search)'''
        possible_numbers = self.possible_numbers.copy()
        for number in line:
            possible_numbers.remove(number) if number != 0 else None        
        return possible_numbers
    
    def check_possible_numbers_in_column(self, possible_numbers: list, my_sudoku: list, column: int) -> list:
        '''returns a list of possible numbers for a blank space (column-search)'''
        column_numbers = []
        choices = possible_numbers.copy()
        for line in my_sudoku:
            column_numbers.append(line[column]) if line[column] != 0 else None
        for item in possible_numbers:
            if item in column_numbers:
                choices.remove(item)
        return choices
    
    def nine_boxes(self, my_sudoku: list):
        '''finds identical numbers per box'''
        boxes = []
        final_boxes = []
        for line in range(0,9):
            for column in range(0,3):
                boxes.append(my_sudoku[line][column*3:(column*3)+3])
        for slice in range(len(boxes)//3):
            print(f"slice {slice}")
            tiny_boxes = []
            tiny_boxes.extend(boxes[slice])
            tiny_boxes.extend(boxes[slice+3])
            tiny_boxes.extend(boxes[slice+6])
            final_boxes.append(tiny_boxes)

        self.board.print_sudoku(final_boxes, "Nine Boxes")
        return final_boxes
    
    def find_duplicate_in_box(self, box: list):
        '''goes through each box and removes duplicates'''
        duplicate_dict = {}
        duplicate_store = []
        for b, box in enumerate(box):
            duplicate_dict[b] = dict(Counter(box))
            for key in duplicate_dict[b]:
                if duplicate_dict[key] >=2:
                    print(1)
        # print(duplicate_store)



    
    
    def check_if_protected(self, coordinate: list):
        '''finds identical numbers per column'''
        board = self.board.create_sudoku_lines(self.sudoku).copy()
        for line in protected_coordinates:
            if coordinate in line:
                return True
        return False
    

class OutputBoard:
    def __init__(self):
        '''methods to reformat the sudoku board'''

    def create_sudoku_board(self) -> list:
        '''creates a 9x9 array of empty lists'''
        sudoku_board = []
        sudoku_temp = []
        for i in range(1,10):
            sudoku_temp.append(self.create_sudoku_box())
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
    
    def create_sudoku_lines(self, sudoku: list) -> list[list]:
        '''prepares a list of lists to print the sudoku numbers per line'''
        sudoku_line = []
        sudoku_lines = []
        for line in sudoku:
            for i in range(3):
                for box in line:
                    sudoku_line.extend(box[i])
                sudoku_lines.append(sudoku_line)
                sudoku_line = []
        return sudoku_lines

    def create_sudoku_columns(self, sudoku: list) -> list[list]:
        '''
        prepares a list of lists to print the sudoku numbers per column
        '''
        sudoku_lines = sudoku.copy()
        temp = []
        columns_to_line = []
        for i in range(0,9):
            for c in range(0,9):
                temp.append(sudoku_lines[c][i])
            columns_to_line.append(temp)
            temp = []
        return columns_to_line
    
    def revert_to_sudoku_lines(self, sudoku: list) -> list[list]:
        '''prepares a list of lists to print the sudoku numbers per line'''
        sudoku_line = []
        sudoku_lines = []
        for line in sudoku:
            for i in range(3):
                for box in line:
                    sudoku_line.extend(box[i])
                sudoku_lines.append(sudoku_line)
                sudoku_line = []
        return sudoku_lines
        
    def print_sudoku(self, sudoku:list, text:str=""):
        '''prints the sudoku'''
        print(text)
        for line in sudoku:
            print(line)
    

su = CreateInitialBoard()