import random
import numpy as np
import os

class SudokuSolver:

    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)


    def check_sequence(self, sequence:np.ndarray):
        return True
        

    def check_one_cell(self, row_index:int , column_index:int):
        return False
        

    def check_row(self, row_index:int):
        pass

    def check_column(self, column_index:int):
        pass 

    def check_block(self, row_index:int, column_index:int):
        pass 

    def solve(self): 
        return False 

    def check_field(self):
        return True
       


def main():    
    sudoku_solver = SudokuSolver()
    
if __name__ == "__main__":
    main()

