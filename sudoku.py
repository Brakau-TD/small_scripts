'''sudoku'''
import pygame
import random
from collections import Counter
import sys

debug_sudoku = [
    [8,1,5,3,9,7,5,7,6],
    [6,2,7,2,4,8,4,8,9],
    [9,3,4,1,5,6,1,3,2],
    [6,1,4,4,1,7,7,2,3],
    [9,8,5,8,3,5,5,4,8],
    [2,7,3,2,9,6,9,6,1],
    [3,5,4,6,1,2,9,4,5],
    [7,6,1,5,7,3,7,8,6],
    [2,9,8,8,4,9,2,3,1]
]

protected_coordinates_2D = [
    [0,1,2],
    [0,1,2],
    [0,1,2],
    [3,4,5],
    [3,4,5],
    [3,4,5],
    [6,7,8],
    [6,7,8],
    [6,7,8]
]


class CreateInitialBoard:
    def __init__(self):
        self.possible_numbers = list(range(1,10))
        self.board = OutputBoard()
        # self.sudoku = self.board.create_sudoku_board()
        self.sudoku = debug_sudoku # for debugging

        self.sudoku = self.construct_first_draft(self.sudoku.copy())
        
        # sudoku_box_lines = self.nine_boxes(sudoku_temp.copy())
        # duplicate_store, boxes = self.find_duplicate_in_box(sudoku_temp.copy())
        # boxes = self.remove_duplicates_from_box(duplicate_store, boxes)
    
    def construct_first_draft(self, sudoku):
        '''
        creates a first draft of the sudoku board
        the board will have 0s in the blank spaces
        but there will be no duplicates in the lines
        either horizontally or vertically
        '''
        sudoku_clean = self.clean_up_initial_sudoku(sudoku)
        sudoku_temp = self.fill_blanks(sudoku_clean.copy())
        sudoku_columns = self.board.create_sudoku_columns(sudoku_temp.copy())
        sudoku_clean = self.clean_up_initial_sudoku(sudoku_columns.copy())
        sudoku_proper_rotation = self.board.create_sudoku_columns(sudoku_clean.copy())
        self.sudoku = sudoku_proper_rotation.copy()

        nine_boxes = self.create_boxes(self.sudoku.copy())
        clean_boxes = self.clean_up_boxes(nine_boxes.copy())
        self.board.print_sudoku(clean_boxes, "clean boxes")
        filled_boxes = self.fill_blanks(clean_boxes.copy())
        self.board.print_sudoku(filled_boxes, "filled boxes")
        sudoku_proper_rotation = self.board.revert_to_sudoku_lines(filled_boxes.copy())
        self.board.print_sudoku(sudoku_proper_rotation, "proper rotation")
        return sudoku_proper_rotation

    def clean_up_initial_sudoku(self, my_sudoku: list):
        '''finds identical numbers in the sudoku and replaces them with 0'''
        board = my_sudoku.copy()
        for l,line in enumerate(my_sudoku):
            for i,item in enumerate(line):
                if line.count(item) > 1 and self.check_if_protected(l,i) is False:
                    board[l][i] = 0
                else:
                    continue
        return board
    
    def clean_up_boxes(self, my_sudoku: list):
        '''finds identical numbers in the sudoku and replaces them with 0'''
        board = my_sudoku.copy()
        for l,line in enumerate(my_sudoku):
            for i,item in enumerate(line):
                if line.count(item) > 1:
                    board[l][i] = 0
                else:
                    continue
        return board
    
    def fill_blanks(self, my_sudoku: list):
        '''takes a sudoku and fills in the blanks'''
        new_sudoku = my_sudoku.copy()
        for l, line in enumerate(my_sudoku):
            for i,item in enumerate(line):
                if item == 0:
                    possible_numbers = self.get_possible_numbers_in_line(line)
                    number = random.choice(possible_numbers) if len(possible_numbers) > 0 else 0
                    new_sudoku[l][i] = number
        return new_sudoku

    
    def get_possible_numbers_in_line(self, line) -> list:
        '''returns a list of possible numbers for a blank space (line-search)'''
        possible_numbers = self.possible_numbers.copy()
        for number in line:
            if number in possible_numbers:
                possible_numbers.remove(number)       
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
    
    def create_boxes(self, my_sudoku: list):
        '''
        cleans up the sudoku by removing duplicates in the boxes
        '''
        nine_boxes = []
        for l in range(3):
            box = []
            for c in range(3):
                column = c*3
                line = l*3
                for i in range(3):
                    box.extend(my_sudoku[line+i][column:column+3])
                nine_boxes.append(box)
                box = []
        return nine_boxes

    
    def find_duplicate_in_box(self, boxes: list):
        '''goes through each box and removes duplicates'''
        duplicate_dict = {}
        duplicate_store = {k:[1 for v in range(9)] for k in range(9)}
        for b, box in enumerate(boxes):
            duplicate_dict[b] = dict(Counter(box))
            for key in duplicate_dict[b]:
                if duplicate_dict[b][key] >=2:
                    duplicate_store[b][key-1] = duplicate_dict[b][key] if key !=0 else 0
        return duplicate_store, boxes
    

    def get_possible_numbers_in_box(self, number, line: list) -> int:
        '''checks for a possible number in a box'''
        choose_from = []
        for item in self.possible_numbers:
            if item in line:
                pass
            else:
                choose_from.append(item)
        number = random.choice(choose_from)
        return number

    def check_if_protected(self, l,i):
        '''finds identical numbers per column'''
        if i in protected_coordinates_2D[l]:
            return True
        return False

    def bloody_shitty_fuckface(self):
        complex = [
            [[8, 1, 5], [9, 2, 4], [6, 3, 8], [2, 5, 9], [4, 1, 7], [7, 2, 3], [3, 8, 4], [6, 8, 2], [9, 4, 5]],
            [[6, 2, 7], [3, 7, 1], [4, 5, 9], [6, 4, 8], [8, 3, 5], [6, 1, 9], [5, 9, 1], [5, 1, 3], [7, 8, 6]],
            [[9, 3, 4], [6, 5, 8], [1, 7, 2], [1, 7, 3], [2, 9, 6], [5, 8, 4], [7, 6, 2], [7, 4, 9], [2, 3, 1]]
            ]
            
        temp = []
        t = []
        final = []

        # item for sublist in l for item in sublist
        for loop in range(3):
            for l,line in enumerate(complex):
                temp = complex[l][loop*3:loop*3+3]
                t.append(temp)
            final.append(t)
            t = []
        finalline = []
        endline = []
        for line in final:
            for sublist in line:
                finalline.extend(sublist)
            endline.extend(finalline)
            finalline = []

        for i in endline:
            print(i)

    

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
        rotates a list, so that all columns become lines
        '''
        sudoku_lines = sudoku.copy()
        new_list = []
        for i in range(9):
            new_list.append([line[i] for line in sudoku_lines])
        return new_list
    
    def revert_to_sudoku_lines(self, boxlists: list):
        '''prepares a list of lists to print the sudoku numbers per line'''
        linie = []
        ergebnis = []
        for i in range(0,9,3):
            for line in range(9):
                linie.append(boxlists[line][i:i+3])
            ergebnis.append(linie)
            linie = []
        return ergebnis

        
    def print_sudoku(self, sudoku:list, text:str=""):
        '''prints the sudoku'''
        print(text)
        for line in sudoku:
            print(line)
        print()
    

su = CreateInitialBoard()
su.bloody_shitty_fuckface()