import numpy as np

BOARD_SIZE = 8 # 8x8 - Normal
BOARD_SIZE = 4 # 4x4 - Generate Simple

class Piece:
    def __init__(self, orientations):
        self.orientations = orientations
        self.orientation_index = 0
        self.orientation = self.orientations[self.orientation_index]
        self.n_orientations = len(self.orientations)
        self.shape = self.orientation.shape
        self.size = np.sum(self.orientation)

    def __repr__(self):
        return str(self.orientation)

    def reorient(self):
        # "Moves the piece into a different orientation by rotating etc."
        self.orientation_index = (1 + self.orientation_index) % self.n_orientations
        self.orientation = self.orientations[self.orientation_index]
        self.shape = self.orientation.shape

    def display(self):
        print(self.orientations[self.orientation_index])

    def get_coords(self):
        # Coordinates for where the piece is occupying space
        return [[r,c] for r,c in np.argwhere(self.orientation!=1)]

    def get_n_orientations(self):
        return self.n_orientations
    
    def get_number(self):
        return np.max(self.orientation)

    def get_orientation(self):
        return self.orientation
    
    def get_orientation_index(self):
        return self.orientation_index
    
    def get_shape(self):
        return self.shape
    
    def get_size(self):
        return self.size
    
    def row(self):
        return self.shape[0]
    
    def column(self):
        return self.shape[1]

class Octogram:
    def __init__(self, pieces):
        self.n_rows = 5
        self.n_cols = 4
        self.board = np.matrix([[0 for i in range(self.n_cols)] for j in range(self.n_rows)]) # 8x8
        self.pieces = pieces

    def generate_pieces(self):
        # Piece 1
        orientations = [
            np.matrix([
                [1, 1],
                [1, 1]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)
        
        # Piece 2
        orientations = [
            np.matrix([
                [0, 2, 0],
                [2, 2, 2],
                [0, 2, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 3
        orientations = [
            np.matrix([
                [3],
                [3],
                [3],
                [3]
            ]),
            np.matrix([
                [3, 3, 3, 3],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 4
        orientations = [
            np.matrix([
                [4, 4],
                [4, 0],
                [4, 4]
            ]),
            np.matrix([
                [4, 4, 4],
                [4, 0, 4]
            ]),
            np.matrix([
                [4, 4],
                [0, 4],
                [4, 4]
            ]),
            np.matrix([
                [4, 0, 4],
                [4, 4, 4]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 5
        orientations = [
            np.matrix([
                [5, 5, 5],
                [0, 5, 0],
                [0, 5, 0]
            ]),
            np.matrix([
                [0, 0, 5],
                [5, 5, 5],
                [0, 0, 5]
            ]),
            np.matrix([
                [0, 5, 0],
                [0, 5, 0],
                [5, 5, 5]
            ]),
            np.matrix([
                [5, 0, 0],
                [5, 5, 5],
                [5, 0, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 6
        orientations = [
            np.matrix([
                [6, 6, 6],
                [6, 0 ,0],
                [6, 0, 0],
            ]),
            np.matrix([
                [6, 6, 6],
                [0, 0 ,6],
                [0, 0, 6],
            ]),
            np.matrix([
                [0, 0, 6],
                [0, 0 ,6],
                [6, 6, 6],
            ]),
            np.matrix([
                [6, 0, 0],
                [6, 0 ,0],
                [6, 6, 6],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 7
        orientations = [
            np.matrix([
                [7, 7, 0],
                [0, 7 ,7],
                [0, 0, 7],
            ]),
            np.matrix([
                [0, 0, 7],
                [0, 7 ,7],
                [7, 7, 0],
            ]),
            np.matrix([
                [7, 0, 0],
                [7, 7 ,0],
                [0, 7, 7],
            ]),
            np.matrix([
                [0, 7, 7],
                [7, 7 ,0],
                [7, 0, 0],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 8
        orientations = [
            np.matrix([
                [8, 0, 0],
                [8, 8, 8],
                [0, 0, 8],
            ]),
            np.matrix([
                [0, 0, 8],
                [8, 8, 8],
                [8, 0, 0],
            ]),
            np.matrix([
                [0, 8, 8],
                [0, 8, 0],
                [8, 8, 0],
            ]),
            np.matrix([
                [8, 8, 0],
                [0, 8, 0],
                [0, 8, 8],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 9
        orientations = [
            np.matrix([
                [9, 0],
                [9, 9],
                [9, 9]
            ]),
            np.matrix([
                [0, 9],
                [9, 9],
                [9, 9]
            ]),
            np.matrix([
                [9, 9],
                [9, 9],
                [0, 9]
            ]),
            np.matrix([
                [9, 9],
                [9, 9],
                [9, 0]
            ]),
                np.matrix([
                [9, 9, 9],
                [9, 9, 0],
            ]),
            np.matrix([
                [9, 9, 9],
                [0, 9, 9],
            ]),
            np.matrix([
                [0, 9, 9],
                [9, 9, 9],
            ]),
            np.matrix([
                [9, 9, 0],
                [9, 9, 9],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 10
        orientations = [
            np.matrix([
                [10, 0],
                [10, 0],
                [10, 10],
                [10, 0]
            ]),
            np.matrix([
                [0, 10],
                [0, 10],
                [10, 10],
                [0, 10]
            ]),
            np.matrix([
                [10, 0],
                [10, 10],
                [10, 0],
                [10, 0]
            ]),
            np.matrix([
                [0, 10],
                [10, 10],
                [0, 10],
                [0, 10]
            ]),
            np.matrix([
                [10, 10, 10, 10],
                [0, 10, 0, 0],
            ]),
            np.matrix([
                [10, 10, 10, 10],
                [0, 0, 10, 0],
            ]),
            np.matrix([
                [0, 10, 0, 0],
                [10, 10, 10, 10],
            ]),
            np.matrix([
                [0, 0, 10, 0],
                [10, 10, 10, 10],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 11
        orientations = [
            np.matrix([
                [0, 11, 0],
                [0, 11, 11],
                [11, 11, 0],
            ]),
            np.matrix([
                [0, 11, 0],
                [11, 11, 0],
                [0, 11, 11],
            ]),
            np.matrix([
                [11, 0, 0],
                [11, 11, 11],
                [0, 11, 0],
            ]),
            np.matrix([
                [0, 0, 11],
                [11, 11, 11],
                [0, 11, 0],
            ]),
            np.matrix([
                [0, 11, 11],
                [11, 11, 0],
                [0, 11, 0],
            ]),
            np.matrix([
                [11, 11, 0],
                [0, 11, 11],
                [0, 11, 0],
            ]),
            np.matrix([
                [0, 11, 0],
                [11, 11, 11],
                [0, 0, 11],
            ]),
            np.matrix([
                [0, 11, 0],
                [11, 11, 11],
                [11, 0, 0],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 12
        orientations = [
            np.matrix([
                [12, 0],
                [12, 0],
                [12, 0],
                [12, 12]
            ]),
            np.matrix([
                [0, 12],
                [0, 12],
                [0, 12],
                [12, 12]
            ]),
            np.matrix([
                [12, 12],
                [12, 0],
                [12, 0],
                [12, 0]
            ]),
            np.matrix([
                [12, 12],
                [0, 12],
                [0, 12],
                [0, 12]
            ]),
            np.matrix([
                [12, 12, 12, 12],
                [12, 0, 0, 0],
            ]),
            np.matrix([
                [12, 12, 12, 12],
                [0, 0, 0, 12],
            ]),
            np.matrix([
                [12, 0, 0, 0],
                [12, 12, 12, 12],
            ]),
            np.matrix([
                [0, 0, 0, 12],
                [12, 12, 12, 12],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 13
        orientations = [
            np.matrix([
                [0, 13],
                [0, 13],
                [13, 13],
                [13, 0]
            ]),
            np.matrix([
                [13, 0],
                [13, 0],
                [13, 13],
                [0, 13]
            ]),
            np.matrix([
                [0, 13],
                [13, 13],
                [13, 0],
                [13, 0]
            ]),
            np.matrix([
                [13, 0],
                [13, 13],
                [0, 13],
                [0, 13]
            ]),
            np.matrix([
                [13, 13, 0, 0],
                [0, 13, 13, 13],
            ]),
            np.matrix([
                [0, 0, 13, 13],
                [13, 13, 13, 0],
            ]),
            np.matrix([
                [13, 13, 13, 0],
                [0, 0, 13, 13],
            ]),
            np.matrix([
                [0, 13, 13, 13],
                [13, 13, 0, 0],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

    def generate_simple(self):
        # 4x4

        # Piece 1
        orientations = [
            np.matrix([
                [1, 1],
                [1, 1]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)
        self.pieces.append(piece)
        self.pieces.append(piece)
        self.pieces.append(piece)

    def generate_small(self):
        # 5x4 - pieces 3, 5, 10, & 12
        # Piece 3
        orientations = [
            np.matrix([
                [3],
                [3],
                [3],
                [3]
            ]),
            np.matrix([
                [3, 3, 3, 3],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 5
        orientations = [
            np.matrix([
                [5, 5, 5],
                [0, 5, 0],
                [0, 5, 0]
            ]),
            np.matrix([
                [0, 0, 5],
                [5, 5, 5],
                [0, 0, 5]
            ]),
            np.matrix([
                [0, 5, 0],
                [0, 5, 0],
                [5, 5, 5]
            ]),
            np.matrix([
                [5, 0, 0],
                [5, 5, 5],
                [5, 0, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 10
        orientations = [
            np.matrix([
                [10, 0],
                [10, 0],
                [10, 10],
                [10, 0]
            ]),
            np.matrix([
                [0, 10],
                [0, 10],
                [10, 10],
                [0, 10]
            ]),
            np.matrix([
                [10, 0],
                [10, 10],
                [10, 0],
                [10, 0]
            ]),
            np.matrix([
                [0, 10],
                [10, 10],
                [0, 10],
                [0, 10]
            ]),
            np.matrix([
                [10, 10, 10, 10],
                [0, 10, 0, 0],
            ]),
            np.matrix([
                [10, 10, 10, 10],
                [0, 0, 10, 0],
            ]),
            np.matrix([
                [0, 10, 0, 0],
                [10, 10, 10, 10],
            ]),
            np.matrix([
                [0, 0, 10, 0],
                [10, 10, 10, 10],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

        # Piece 12
        orientations = [
            np.matrix([
                [12, 0],
                [12, 0],
                [12, 0],
                [12, 12]
            ]),
            np.matrix([
                [0, 12],
                [0, 12],
                [0, 12],
                [12, 12]
            ]),
            np.matrix([
                [12, 12],
                [12, 0],
                [12, 0],
                [12, 0]
            ]),
            np.matrix([
                [12, 12],
                [0, 12],
                [0, 12],
                [0, 12]
            ]),
            np.matrix([
                [12, 12, 12, 12],
                [12, 0, 0, 0],
            ]),
            np.matrix([
                [12, 12, 12, 12],
                [0, 0, 0, 12],
            ]),
            np.matrix([
                [12, 0, 0, 0],
                [12, 12, 12, 12],
            ]),
            np.matrix([
                [0, 0, 0, 12],
                [12, 12, 12, 12],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

    def solve_octogram(self):
        pieces = set(range(len(self.pieces)))
        if self.solve(r=0, c=0, pieces=pieces):
            print("great success!")
            self.show_solution()
        else:
            print('No solution found...')

    def solve(self, r, c, pieces):
        print(r,c)
        print(self.board)
        print("")
        # base case
        if r == self.n_rows:
            r = 0
            c += 1
            if c == self.n_cols:
                return True

        # recursive case
        if self.board[r, c] != 0:
            return self.solve(r + 1, c, pieces)

        # consider all available pieces to place on board
        for _ in range(len(pieces)):
            i = pieces.pop()
            p = self.pieces[i]

            # Now consider all possible orientations for that piece
            for j in range(p.get_n_orientations()):
                if self.is_valid(r, c, p):
                    self.place_piece(r, c, p)

                    if self.solve(r + 1, c, pieces):
                        return True
                    
                    # backtrack
                    self.remove_piece(r, c, p)
                    pieces.add(i)
                    p.reorient()

        return False

    def is_valid(self, r, c, piece):
        ixs = piece.get_coords()
        board_coords = [[r + p_r, c + p_c] for p_r, p_c in ixs]

        # Check all rows are in-bounds
        rows = [x[0] for x in board_coords]
        if np.max(rows) >= self.n_rows:
            return False

        # Check all columns are in-bounds
        cols = [x[1] for x in board_coords]
        if np.max(cols) >= self.n_cols:
            return False

        # Check that there is an empty space in each co-ordinate this piece will occupy.
        return np.sum([self.board[b_r, b_c] for b_r, b_c in board_coords]) == 0

    def place_piece(self, r, c, piece):        
        # Indexes that the piece "occupies the space of"
        ixs = piece.get_coords()

        # Coordinates of the board to update to 1
        board_coords = [[r + p_r, c + p_c] for p_r, p_c in ixs]

        for coord in board_coords:
            x, y = coord
            self.board[x, y] = piece.get_number()

    def remove_piece(self, r, c, piece):
        # Indexes that the piece "occupies the space of"
        ixs = piece.get_coords()

        # Coordinates of the board to make zero
        board_coords = [[r + p_r, c + p_c] for p_r, p_c in ixs]

        for coord in board_coords:
            x, y = coord
            if x >= BOARD_SIZE:
                print(x, y)
            if y >= BOARD_SIZE:
                print(x,y)
            self.board[x, y] = 0

    def show_solution(self):
        print(self.board)


if __name__ == '__main__':
    octogram = Octogram(pieces=[])
    octogram.generate_small()
    octogram.solve_octogram()
