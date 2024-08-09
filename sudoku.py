BOARD_SIZE = 9
MIN_NUM = 1
MAX_NUM = 9
BOX_SIZE = 3

class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid

    def solve_sudoku(self):
        if self.solve(0, 0):
            self.show_solution()
        else:
            print('No solution found...')

    def solve(self, r, c):
        # base case
        if r == BOARD_SIZE:
            r = 0
            c += 1
            if c == BOARD_SIZE:
                return True

        # recursive case
        if self.grid[r][c] != 0:
            return self.solve(r + 1, c)

        # consider numbers 1-9
        for n in range(MIN_NUM, MAX_NUM+1):
            if self.is_valid(r, c, n):
                self.grid[r][c] = n

                if self.solve(r + 1, c):
                    return True

                # backtrack
                self.grid[r][c] = 0

        return False

    def is_valid(self, r, c, n):
        # check row
        for i in range(BOARD_SIZE):
            if self.grid[i][c] == n:
                return False

        # check column
        for j in range(BOARD_SIZE):
            if self.grid[r][j] == n:
                return False

        # check 3x3
        row_offset = (r // 3) * BOX_SIZE
        col_offset = (c // 3) * BOX_SIZE

        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if self.grid[row_offset + i][col_offset + j] == n:
                    return False

        return True
    
    def show_solution(self):
        for r in range(9):
            for c in range(9):
                print(self.grid[r][c], end=' ')
            print('')


if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    sudoku = SudokuSolver(grid=grid)
    sudoku.solve_sudoku()
    