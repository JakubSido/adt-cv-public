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

    
    def load(self, file_path:str):
        loaded_rows = list()
        with open(file_path, encoding="utf-8") as f:
            for line in f.read().splitlines():
                loaded_rows.append([int(cell) for cell in line.split(";")])
        self.field = np.array(loaded_rows)

    def save(self, file_path:str):
        with open(file_path, "w", encoding="utf-8") as f:
            for row_index in range(self.n_rows):
                row = self.field[row_index]
                f.write(";".join([str(number) for number in row]) + "\n")
    

    def check_sequence(self, sequence:np.ndarray):
        
        contains = set()
        for cell in sequence:
            if cell == 0:  # není vyplněno
                continue
            if cell in contains:  # neco vicekrat
                return False
            contains.add(cell)
        
        return True
        

    def check_one_cell(self, row_index:int , column_index:int):
        
        if self.check_row(row_index) & self.check_column(column_index) & self.check_block(row_index, column_index):
            return True
        
        return False
        

    def check_row(self, row_index:int):
        
        row = self.field[row_index, :]
        return self.check_sequence(row)
        
        pass

    def check_column(self, column_index:int):
        
        column = self.field[:, column_index]
        return self.check_sequence(column)
        
        pass

    def check_block(self, row_index:int, column_index:int):
        
        row_start = (row_index // 3) * 3
        column_start = (column_index // 3) * 3
        block = self.field[row_start: row_start + 3, column_start: column_start + 3]
        return self.check_sequence(block.reshape(-1))
        
        pass

    def solve(self): 
        
        for r in range(9):
            for c in range(9):
                if self.field[r][c] != EMPTY_VALUE:  
                    if r == 8 and c == 8:  # mame vyreseno
                        return True
                    continue
                numbers = [i for i in range(1, 10)]
                random.shuffle(numbers)
                for value in numbers:
                    self.field[r][c] = value
                    if not self.check_one_cell(r, c):
                        continue
                    solved = self.solve()
                    if solved:
                        return True
                    
                self.field[r][c] = EMPTY_VALUE
                return False
        

    def check_field(self):
        
        for r in range(self.n_rows):
            if not self.check_row(r):
                return False
        for c in range(self.n_columns):
            if not self.check_column(c):
                return False

        for r in range(0, self.n_rows, 3):
            for c in range(0, self.n_columns, 3):
                if not self.check_block(r, c):
                    return False
        
        return True
       


def main():    
    sudoku_solver = SudokuSolver()
    # sudoku_solver.load("sudoku.csv")
    
    print(sudoku_solver.solve())
    print(sudoku_solver.field)
    
if __name__ == "__main__":
    main()

