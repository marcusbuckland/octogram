import numpy as np
import random

BOARD_SIZE = 8

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
        return [[r, c] for r, c in np.argwhere(self.orientation != 0)]

    def get_n_orientations(self):
        return self.n_orientations
    
    def get_number(self):
        return np.max(self.orientation)

    def get_orientation(self):
        return self.orientation
    
    def get_orientations(self):
        return self.orientations
    
    def get_orientation_index(self):
        return self.orientation_index
    
    def get_shape(self):
        return self.shape
    
    def get_size(self):
        return self.size
    
    def get_row_offset(self):
        return -np.min(np.where(self.get_orientation()[:,0] == self.get_number())[0]) # lol

    def row(self):
        return self.shape[0]
    
    def column(self):
        return self.shape[1]

class Octogram:
    def __init__(self):
        self.n_rows = BOARD_SIZE
        self.n_cols = BOARD_SIZE
        self.board = np.matrix([[0 for i in range(self.n_cols)] for j in range(self.n_rows)]) # 8x8
        self.pieces = []

    def __repr__(self):
        return str(self.board)

    def generate_pieces(self):
        self.pieces = []

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
                [3],
                [3]
            ]),
            np.matrix([
                [3, 3, 3, 3, 3],
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

    def get_board_coords(self, r, c, piece, orientation):
        piece_coords = self.get_piece_coords(orientation)
        row_offset = self.get_row_offset(piece, orientation)
        return [[r + p_r - row_offset, c + p_c] for p_r, p_c in piece_coords]

    def get_piece_coords(self, orientation):
        return [[r, c] for r, c in np.argwhere(orientation != 0)]

    def get_row_offset(self, piece, orientation):
        return np.min(np.where(orientation[:,0] == piece.get_number())[0]) # lol

    def solve_cross(self):
        self.n_rows = 9
        self.n_cols = 9
        self.board = np.matrix([[0 for i in range(self.n_cols)] for j in range(self.n_rows)]) # 9x9 with empty space
        
        # Empty space piece
        orientations = np.matrix([[-1 for i in range(3)] for j in range(3)]) # 3x3
        piece = Piece(orientations=[orientations])
        self.place_piece(r=0,c=0, piece=piece, orientation=piece.orientation)
        self.place_piece(r=6,c=0, piece=piece, orientation=piece.orientation)
        self.place_piece(r=0,c=6, piece=piece, orientation=piece.orientation)
        self.place_piece(r=6,c=6, piece=piece, orientation=piece.orientation)

        pieces_required = [3, 4, 5, 6, 8, 9, 10, 11, 12]
        self.pieces = [p for p in self.pieces if p.get_number() in pieces_required]

        if self.solve(r=0, c=0):
            print("Solution for Cross:")
            print(self.board)
        else:
            print('No solution found...')

    def solve_octogram(self):
        if self.solve(r=0, c=0):
            print("Solution for Octogram:")
            print(self.board)
            print("")
        else:
            print('No solution found...')

    def solve_rectangle(self):
        self.n_rows = 4
        self.n_cols = 15
        self.board = np.matrix([[0 for i in range(self.n_cols)] for j in range(self.n_rows)]) # 4x15

        pieces_required = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.pieces = [p for p in self.pieces if p.get_number() in pieces_required]

        if self.solve(r=0, c=0):
            print("Solution for Rectangle!")
            print(self.board)
            print("")
        else:
            print('No solution found...')

    def solve_zig_zag(self):
        self.n_rows = 9
        self.n_cols = 9
        self.board = np.matrix([[0 for i in range(self.n_cols)] for j in range(self.n_rows)]) # 9x9 with empty space
        
        # Empty space piece
        orientations = np.matrix([[-1 for i in range(3)] for j in range(3)]) # 3x3
        piece = Piece(orientations=[orientations])
        self.place_piece(r=6,c=0, piece=piece, orientation=piece.orientation)
        self.place_piece(r=0,c=3, piece=piece, orientation=piece.orientation)
        self.place_piece(r=0,c=6, piece=piece, orientation=piece.orientation)
        self.place_piece(r=3,c=6, piece=piece, orientation=piece.orientation)

        pieces_required = [3, 4, 5, 6, 8, 9, 10, 11, 12]
        self.pieces = [p for p in self.pieces if p.get_number() in pieces_required]

        if self.solve(r=0, c=0):
            print("Solution for Zig-zag:")
            print(self.board)
        else:
            print('No solution found...')

    def solve(self, r, c): 
        # base case
        if r == self.n_rows:
            r = 0
            c += 1
            if c == self.n_cols:
                return True # Solution found!

        # recursive case
        if self.board[r, c] != 0:
            return self.solve(r + 1, c)

        # consider all available pieces to place on board
        for p in self.get_valid_pieces():
            # Now consider all possible orientations for that piece
            for orientation in p.get_orientations():
                if self.is_valid(r, c, p, orientation):
                    self.place_piece(r, c, p, orientation)

                    if self.solve(r + 1, c):
                        return True
                    
                    # backtrack
                    self.remove_piece(p)

        return False

    def get_valid_pieces(self):
        pieces_on_board = [p for p in np.unique(np.array(octogram.board)) if p != 0]
        return [p for p in octogram.pieces if p.get_number() not in pieces_on_board]
        
    def is_valid(self, r, c, piece, orientation):
        # If the piece has already been placed, it isn't valid.
        if piece.get_number() in self.board:
            return False
        
        board_coords = self.get_board_coords(r, c, piece, orientation)        
        for b_r, b_c in board_coords:
            # Check all rows are in-bounds
            if b_r >= self.n_rows or b_r < 0:
                return False
            
            # Check all columns are in-bounds
            if b_c >= self.n_cols or b_c < 0:
                return False
            
            # Check that there is an empty space in each coordinate this piece will occupy
            if self.board[b_r, b_c] != 0:
                return False

        return True

    def place_piece(self, r, c, piece, orientation):
        board_coords = self.get_board_coords(r, c, piece, orientation)
        for r, c in board_coords:
            self.board[r, c] = piece.get_number()

    def remove_piece(self, piece):
        self.board[np.where(self.board==piece.get_number())] = 0

if __name__ == '__main__':
    octogram = Octogram()
    octogram.generate_pieces()
    random.shuffle(octogram.pieces)
    # octogram.solve_octogram()
    # octogram.solve_cross()
    # octogram.solve_rectangle()
    # octogram.solve_zig_zag()