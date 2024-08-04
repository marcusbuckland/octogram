import numpy as np

BOARD_SIZE = 8 # 8x8

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
        self.orientation_index = (1 + self.orientation_index) % self.n_orientations
        self.orientation = self.orientations[self.orientation_index]
        self.shape = self.orientation.shape

    def display(self):
        print(self.orientations[self.orientation_index])

    def get_coords(self):
        # Coordinates for where the piece is occupying space
        return [[r,c] for r,c in np.argwhere(self.orientation==1)]

    def get_n_orientations(self):
        return self.n_orientations

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
    def __init__(self):
        self.n_rows = BOARD_SIZE
        self.n_cols = BOARD_SIZE
        self.board = np.matrix([[0 for i in range(self.n_rows)] for j in range(self.n_cols)]) # 8x8
        self.available_pieces = []

    def generate_pieces(self):
        # Piece 1
        orientations = [
            np.matrix([
                [1, 1],
                [1, 1]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)
        
        # Piece 2
        orientations = [
            np.matrix([
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 3
        orientations = [
            np.matrix([
                [1],
                [1],
                [1],
                [1]
            ]),
            np.matrix([
                [1, 1, 1, 1],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 4
        orientations = [
            np.matrix([
                [1, 1],
                [1, 0],
                [1, 1]
            ]),
            np.matrix([
                [1, 1, 1],
                [1, 0, 1]
            ]),
            np.matrix([
                [1, 1],
                [0, 1],
                [1, 1]
            ]),
            np.matrix([
                [1, 0, 1],
                [1, 1, 1]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 5
        orientations = [
            np.matrix([
                [1, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
            ]),
            np.matrix([
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 1]
            ]),
            np.matrix([
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 1]
            ]),
            np.matrix([
                [1, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 6
        orientations = [
            np.matrix([
                [1, 1, 1],
                [1, 0 ,0],
                [1, 0, 0],
            ]),
            np.matrix([
                [1, 1, 1],
                [0, 0 ,1],
                [0, 0, 1],
            ]),
            np.matrix([
                [0, 0, 1],
                [0, 0 ,1],
                [1, 1, 1],
            ]),
            np.matrix([
                [1, 0, 0],
                [1, 0 ,0],
                [1, 1, 1],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 7
        orientations = [
            np.matrix([
                [1, 1, 0],
                [0, 1 ,1],
                [0, 0, 1],
            ]),
            np.matrix([
                [0, 0, 1],
                [0, 1 ,1],
                [1, 1, 0],
            ]),
            np.matrix([
                [1, 0, 0],
                [1, 1 ,0],
                [0, 1, 1],
            ]),
            np.matrix([
                [0, 1, 1],
                [1, 1 ,0],
                [1, 0, 0],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 8
        orientations = [
            np.matrix([
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 1],
            ]),
            np.matrix([
                [0, 0, 1],
                [1, 1, 1],
                [1, 0, 0],
            ]),
            np.matrix([
                [0, 1, 1],
                [0, 1, 0],
                [1, 1, 0],
            ]),
            np.matrix([
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 1],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 9
        orientations = [
            np.matrix([
                [1, 0],
                [1, 1],
                [1, 1]
            ]),
            np.matrix([
                [0, 1],
                [1, 1],
                [1, 1]
            ]),
            np.matrix([
                [1, 1],
                [1, 1],
                [0, 1]
            ]),
            np.matrix([
                [1, 1],
                [1, 1],
                [1, 0]
            ]),
                np.matrix([
                [1, 1, 1],
                [1, 1, 0],
            ]),
            np.matrix([
                [1, 1, 1],
                [0, 1, 1],
            ]),
            np.matrix([
                [0, 1, 1],
                [1, 1, 1],
            ]),
            np.matrix([
                [1, 1, 0],
                [1, 1, 1],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 10
        orientations = [
            np.matrix([
                [1, 0],
                [1, 0],
                [1, 1],
                [1, 0]
            ]),
            np.matrix([
                [0, 1],
                [0, 1],
                [1, 1],
                [0, 1]
            ]),
            np.matrix([
                [1, 0],
                [1, 1],
                [1, 0],
                [1, 0]
            ]),
            np.matrix([
                [0, 1],
                [1, 1],
                [0, 1],
                [0, 1]
            ]),
            np.matrix([
                [1, 1, 1, 1],
                [0, 1, 0, 0],
            ]),
            np.matrix([
                [1, 1, 1, 1],
                [0, 0, 1, 0],
            ]),
            np.matrix([
                [0, 1, 0, 0],
                [1, 1, 1, 1],
            ]),
            np.matrix([
                [0, 0, 1, 0],
                [1, 1, 1, 1],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 11
        orientations = [
            np.matrix([
                [0, 1, 0],
                [0, 1, 1],
                [1, 1, 0],
            ]),
            np.matrix([
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 1],
            ]),
            np.matrix([
                [1, 0, 0],
                [1, 1, 1],
                [0, 1, 0],
            ]),
            np.matrix([
                [0, 0, 1],
                [1, 1, 1],
                [0, 1, 0],
            ]),
            np.matrix([
                [0, 1, 1],
                [1, 1, 0],
                [0, 1, 0],
            ]),
            np.matrix([
                [1, 1, 0],
                [0, 1, 1],
                [0, 1, 0],
            ]),
            np.matrix([
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 1],
            ]),
            np.matrix([
                [0, 1, 0],
                [1, 1, 1],
                [1, 0, 0],
            ]),
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 12
        orientations = [
            np.matrix([
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 1]
            ]),
            np.matrix([
                [0, 1],
                [0, 1],
                [0, 1],
                [1, 1]
            ]),
            np.matrix([
                [1, 1],
                [1, 0],
                [1, 0],
                [1, 0]
            ]),
            np.matrix([
                [1, 1],
                [0, 1],
                [0, 1],
                [0, 1]
            ]),
            np.matrix([
                [1, 1, 1, 1],
                [1, 0, 0, 0],
            ]),
            np.matrix([
                [1, 1, 1, 1],
                [0, 0, 0, 1],
            ]),
            np.matrix([
                [1, 0, 0, 0],
                [1, 1, 1, 1],
            ]),
            np.matrix([
                [0, 0, 0, 1],
                [1, 1, 1, 1],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

        # Piece 13
        orientations = [
            np.matrix([
                [0, 1],
                [0, 1],
                [1, 1],
                [1, 0]
            ]),
            np.matrix([
                [1, 0],
                [1, 0],
                [1, 1],
                [0, 1]
            ]),
            np.matrix([
                [0, 1],
                [1, 1],
                [1, 0],
                [1, 0]
            ]),
            np.matrix([
                [1, 0],
                [1, 1],
                [0, 1],
                [0, 1]
            ]),
            np.matrix([
                [1, 1, 0, 0],
                [0, 1, 1, 1],
            ]),
            np.matrix([
                [0, 0, 1, 1],
                [1, 1, 1, 0],
            ]),
            np.matrix([
                [1, 1, 1, 0],
                [0, 0, 1, 1],
            ]),
            np.matrix([
                [0, 1, 1, 1],
                [1, 1, 0, 0],
            ])
        ]
        piece = Piece(orientations=orientations)
        self.available_pieces.append(piece)

    def solve_octogram(self):
        if self.solve(r=0, c=0):
            self.show_solution()
        else:
            print('No solution found...')

    def solve(self, r, c):
        # base case
        if r == self.n_rows:
            c += 1
            if c == self.n_cols:
                return True
            else:
                r = 0

        # recursive case
        if self.board[r, c] != 0:
            return self.solve(r + 1, c)

        # consider pieces to place on board
        for p in self.available_pieces:
            if self.is_valid(r, c, p):
                self.place_piece(r, c, p)

                if self.solve(r + 1, c):
                    return True

                # backtrack
                self.remove_piece(r, c, p)
                p.reorient()

        return False

    def is_valid(self, r, c, piece):
        # Check row isn't out of bounds
        if r + piece.row() > BOARD_SIZE:
            return False

        # Check column isn't out bounds
        if c + piece.column() > BOARD_SIZE:
            return False

        # Now check that there is space on the board for the piece to fit into.
        ixs = piece.get_coords()
        
        board_coords = [[r+p_r, c+p_c] for p_r, p_c in ixs]
        return np.sum([self.board[b_r, b_c] for b_r, b_c in board_coords]) == 0

    def place_piece(self, r, c, piece):
        # Remove from available pieces as piece cannot be used more than once.
        self.available_pieces.remove(piece)
        
        # Indexes that the piece "occupies the space of"
        ixs = piece.get_coords()

        # Coordinates of the board to update to 1
        board_coords = [[r+p_r, c+p_c] for p_r, p_c in ixs]

        for coord in board_coords:
            r, c = coord
            self.board[r,c] = 1

    def remove_piece(self, r, c, piece):
        self.available_pieces.append(piece)
        
        # Indexes that the piece "occupies the space of"
        ixs = piece.get_coords()

        # Coordinates of the board to make zero
        board_coords = [[r+p_r, c+p_c] for p_r, p_c in ixs]

        for coord in board_coords:
            r, c = coord
            self.board[r,c] = 0

    def show_solution(self):
        print(self.board)


if __name__ == '__main__':
    octogram = Octogram()
    octogram.generate_pieces()
    octogram.solve_octogram()
    
