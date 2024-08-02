import numpy as np

class Piece:
    def __init__(self, orientations):
        self.orientations = orientations
        self.orientation_index = 0
        self.orientation = self.orientations[self.orientation_index]
        self.n_orientations = len(self.orientations)
        self.shape = self.orientation.shape
        self.size = np.sum(self.orientation)

    def __repr__(self):
        return str(self.orientations[self.orientation_index])

    def reorient(self):
        self.orientation_index = (1 + self.orientation_index) % self.n_orientations

    def display(self):
        print(self.orientations[self.orientation_index])

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


class Octogram:
    def __init__(self, pieces):
        self.n_rows = 8
        self.n_cols = 8
        self.board = [[0 for i in range(self.n_rows)] for j in range(self.n_cols)]
        self.available_pieces = pieces
        self.unavailable_pieces = []

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
        # Base Case


        # Recursive Case
        pass


    
