import random
import numpy as np
import os

class SudokuSolver:

    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    
    def load(self, file_path:str):
        loaded_rows = list()
        with open(file_path, encoding="utf-8") as f:
            for line in f.read().splitlines():
                loaded_rows.append([int(cell) for cell in line.split(";")])
        self.field = np.array(loaded_rows)

    def save(self, file_path:str):
        with open(file_path, "w", encoding="utf-8") as f:
            for row_index in range(9):
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
        
        if self.check_row(row_index) and self.check_column(column_index) and self.check_block(row_index, column_index):
            return True
        
        return False
        

    def check_row(self, row_index:int):
        
        row = self.field[row_index, :]
        return self.check_sequence(row)
        
        pass

    def check_column(self, column_index:int):
        
        column = self.field[:, column_index]
        return self.check_sequence(column)
        

    def check_block(self, row_index:int, column_index:int):
        
        row_start = (row_index // 3) * 3
        column_start = (column_index // 3) * 3
        block = self.field[row_start: row_start + 3, column_start: column_start + 3]
        return self.check_sequence(block.reshape(-1))
        

    def solve(self): 
        
        for r in range(9):
            for c in range(9):
                if self.field[r][c] != 0:  
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
                    
                self.field[r][c] = 0
                return False
        

    def check_field(self):
        
        for r in range(9):
            if not self.check_row(r):
                return False
        for c in range(9):
            if not self.check_column(c):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not self.check_block(r, c):
                    return False
        
        return True
       


def main():    
    sudoku_solver = SudokuSolver()
    
    for sudoku_file in os.listdir("data"):
        file = os.path.join("data", sudoku_file)
        print("solving: ", file)
        sudoku_solver.load(file)
        print(sudoku_solver.solve())
        print(sudoku_solver.field)
    
    
if __name__ == "__main__":
    main()

