from collections import deque
import numpy as np


class CubeMoves:
    def __init__(self):
        self.moves = deque()

    def add_move(self, move):
        self.moves.append(move)

        return self

    def execute_moves(self, cube, solve=True):

        if solve is True:
            while self.moves:
                move = self.moves.popleft()
                self._perform_move(cube, move)

        else:
            if self.moves:
                move = self.moves.popleft()
                self._perform_move(cube, move)

    def _perform_move(self, cube, move):
        faces = ['F', 'B', 'L', 'R', 'U', 'D']

        if "'" not in move and "2" not in move:  # 90 degrees clockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True)
        elif "'" in move:  # 90 degrees counterclockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=False)
        elif "2" in move:  # 180 degrees clockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True, double=True)

    @staticmethod
    def _rotate_cube(cube, face, clockwise=True, double=False):

        if clockwise is True and double is False:
            if face == "U":

                front_prev = cube.Front.copy()

                cube.Upper = np.rot90(cube.Upper, 1, (1, 0))

                cube.Front[0] = cube.Right[0]
                cube.Right[0] = cube.Back[0]
                cube.Back[0] = cube.Left[0]
                cube.Left[0] = front_prev[0]

            elif face == "D":

                front_prev = cube.Front.copy()

                cube.Lower = np.rot90(cube.Lower, 1, (1, 0))

                cube.Front[2] = cube.Left[2]
                cube.Left[2] = cube.Back[2]
                cube.Back[2] = cube.Right[2]
                cube.Right[2] = front_prev[2]

            elif face == "L":

                front_prev = cube.Front.copy()

                cube.Left = np.rot90(cube.Left, 1, (1, 0))

                cube.Front[:, 0] = cube.Upper[:, 0]
                cube.Upper[:, 0] = cube.Back[::-1, 2]
                cube.Back[:, 2] = cube.Lower[::-1, 0]
                cube.Lower[:, 0] = front_prev[:, 0]

            elif face == "R":

                front_prev = cube.Front.copy()

                cube.Right = np.rot90(cube.Right, 1, (1, 0))

                cube.Front[:, 2] = cube.Lower[:, 2]
                cube.Lower[:, 2] = cube.Back[::-1, 0]
                cube.Back[:, 0] = cube.Upper[::-1, 2]
                cube.Upper[:, 2] = front_prev[:, 2]

            elif face == "F":
                upper_prev = cube.Upper.copy()

                cube.Front = np.rot90(cube.Front, 1, (1, 0))

                cube.Upper[2] = cube.Left[::-1, 2]
                cube.Left[:, 2] = cube.Lower[0]
                cube.Lower[0] = cube.Right[::-1, 0]
                cube.Right[:, 0] = upper_prev[2]

            elif face == "B":

                upper_prev = cube.Upper.copy()

                cube.Back = np.rot90(cube.Back, 1, (1, 0))

                cube.Upper[0] = cube.Right[:, 2]
                cube.Right[:, 2] = cube.Lower[2, ::-1]
                cube.Lower[2] = cube.Left[:, 0]
                cube.Left[:, 0] = upper_prev[0, ::-1]

