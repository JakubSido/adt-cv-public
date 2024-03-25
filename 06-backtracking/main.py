import random
import numpy as np

EMPTY_VALUE = 0

class SudokuSolver:

    def __init__(self, field:np.ndarray|None=None, n_rows:int=9, n_columns:int=9):

        if field is None:
            field = np.zeros([n_rows, n_columns], dtype=int)
        self.field = field
        self.n_rows = n_rows
        self.n_columns = n_columns


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
    # sudoku_solver.load("sudoku.csv")
    
    print(sudoku_solver.solve())
    print(sudoku_solver.field)
    
if __name__ == "__main__":
    main()

