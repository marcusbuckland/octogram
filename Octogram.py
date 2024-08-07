import numpy as np

BOARD_SIZE = 8 # 8x8 - Normal
BOARD_SIZE = 4 # 4x4 - Generate Simple

# Generate small
# n_rows = 5
# n_cols = 4

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
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]
            ])
        ]
        piece = Piece(orientations=orientations)
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

    def generate_simple(self):
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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
        self.pieces.append(piece)

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
            p = self.available_pieces[i]

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
            self.board[x, y] = 1

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
    octogram = Octogram()
    octogram.generate_small()
    octogram.solve_octogram()
