from collections import deque
import numpy as np


class CubeMoves:
    def __init__(self):
        """
            Initializes a CubeMoves object with an empty deque to store moves.
        """
        self.moves = deque()

    def add_moves(self, moves):
        """
            Adds moves to the deque. Parses input string to handle multiple moves.

            Args:
            - moves (str): A string representing the moves. Can include space-separated moves.

            Returns:
            The CubeMoves object for method chaining.
        """
        if " " in moves:
            moves_list = moves.split(" ")
            for move in moves_list:
                self.moves.append(move)
        else:
            self.moves.append(moves)
        return self

    def execute_moves(self, cube, copy=False):
        """
            Executes the moves on the provided Cube object.

            Args:
            - cube_modules (Cube): The Cube object on which moves will be executed.
            - solve (bool): If True, executes moves until the deque is empty, else executes a single move.

            Returns:
            None
        """
        if copy is False:
            while self.moves:
                move = self.moves.popleft()
                self._perform_move(cube, move)
                cube.history.append(move)
        else:
            temp = self.moves.copy()
            while temp:
                move = temp.popleft()
                self._perform_move(cube, move)
                cube.history.append(move)

    def _perform_move(self, cube, move):
        """
            Performs a single move on the provided Cube object.

            Args:
            - cube_modules (Cube): The Cube object on which the move will be performed.
            - move (str): The move to be executed.

            Returns:
            None
        """
        faces = ['F', 'B', 'L', 'R', 'U', 'D']
        face = move[0]

        if "'" not in move and "2" not in move:  # 90 degrees clockwise
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True)
        elif "'" in move and "2" not in move:  # 90 degrees counterclockwise
            if face in faces:
                self._rotate_cube(cube, face, clockwise=False)
        elif "2" in move and "'" not in move:  # 180 degrees clockwise
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True, double=True)
        elif "2" in move and "'" in move:  # 180 degrees counterclockwise
            if face in faces:
                self._rotate_cube(cube, face, clockwise=False, double=True)

    @staticmethod
    def _rotate_cube(cube, face, clockwise=True, double=False):
        """
            Rotates the cube_modules's face either clockwise, counterclockwise, or 180 degrees based on input parameters.

            Args:
            - cube (Cube): The Cube object on which the rotation will be performed.
            - face (str): The face of the cube_modules to be rotated.
            - clockwise (bool): If True, rotates the face clockwise. If False, rotates counterclockwise.
            - double (bool): If True, rotates the face by 180 degrees.

            Returns:
            None
        """

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

        elif double is True:

            if face == "U":

                front_prev = cube.Front.copy()
                right_prev = cube.Right.copy()

                cube.Upper = np.rot90(cube.Upper, 2, (1, 0))

                cube.Front[0] = cube.Back[0]
                cube.Right[0] = cube.Left[0]
                cube.Back[0] = front_prev[0]
                cube.Left[0] = right_prev[0]

            elif face == "D":

                front_prev = cube.Front.copy()
                right_prev = cube.Right.copy()

                cube.Lower = np.rot90(cube.Lower, 2, (1, 0))

                cube.Front[2] = cube.Back[2]
                cube.Right[2] = cube.Left[2]
                cube.Back[2] = front_prev[2]
                cube.Left[2] = right_prev[2]

            elif face == "L":

                front_prev = cube.Front.copy()
                upper_prev = cube.Upper.copy()

                cube.Left = np.rot90(cube.Left, 2, (1, 0))

                cube.Front[:, 0] = cube.Back[::-1, 2]
                cube.Upper[:, 0] = cube.Lower[:, 0]
                cube.Back[:, 2] = front_prev[::-1, 0]
                cube.Lower[:, 0] = upper_prev[:, 0]

            elif face == "R":

                front_prev = cube.Front.copy()
                upper_prev = cube.Upper.copy()

                cube.Right = np.rot90(cube.Right, 2, (1, 0))

                cube.Front[:, 2] = cube.Back[::-1, 0]
                cube.Upper[:, 2] = cube.Lower[:, 2]
                cube.Back[:, 0] = front_prev[::-1, 2]
                cube.Lower[:, 2] = upper_prev[:, 2]

            elif face == "F":

                upper_prev = cube.Upper.copy()
                left_prev = cube.Left.copy()

                cube.Front = np.rot90(cube.Front, 2, (1, 0))

                cube.Upper[2] = cube.Lower[0, ::-1]
                cube.Left[:, 2] = cube.Right[::-1, 0]
                cube.Lower[0] = upper_prev[2, ::-1]
                cube.Right[:, 0] = left_prev[::-1, 2]

            elif face == "B":

                upper_prev = cube.Upper.copy()
                left_prev = cube.Left.copy()

                cube.Back = np.rot90(cube.Back, 2, (1, 0))

                cube.Upper[0] = cube.Lower[2, ::-1]
                cube.Left[:, 0] = cube.Right[::-1, 2]
                cube.Lower[2] = upper_prev[0, ::-1]
                cube.Right[:, 2] = left_prev[::-1, 0]

        elif clockwise is False and double is False:

            if face == "U":

                front_prev = cube.Front.copy()

                cube.Upper = np.rot90(cube.Upper, 1, (0, 1))

                cube.Front[0] = cube.Left[0]
                cube.Left[0] = cube.Back[0]
                cube.Back[0] = cube.Right[0]
                cube.Right[0] = front_prev[0]

            elif face == "D":

                front_prev = cube.Front.copy()

                cube.Lower = np.rot90(cube.Lower, 1, (0, 1))

                cube.Front[2] = cube.Right[2]
                cube.Right[2] = cube.Back[2]
                cube.Back[2] = cube.Left[2]
                cube.Left[2] = front_prev[2]

            elif face == "L":

                front_prev = cube.Front.copy()

                cube.Left = np.rot90(cube.Left, 1, (0, 1))

                cube.Front[:, 0] = cube.Lower[:, 0]
                cube.Lower[:, 0] = cube.Back[::-1, 2]
                cube.Back[:, 2] = cube.Upper[::-1, 0]
                cube.Upper[:, 0] = front_prev[:, 0]

            elif face == "R":

                front_prev = cube.Front.copy()

                cube.Right = np.rot90(cube.Right, 1, (0, 1))

                cube.Front[:, 2] = cube.Upper[:, 2]
                cube.Upper[:, 2] = cube.Back[::-1, 0]
                cube.Back[:, 0] = cube.Lower[::-1, 2]
                cube.Lower[:, 2] = front_prev[:, 2]

            elif face == "F":
                upper_prev = cube.Upper.copy()

                cube.Front = np.rot90(cube.Front, 1, (0, 1))

                cube.Upper[2] = cube.Right[:, 0]
                cube.Right[:, 0] = cube.Lower[0, ::-1]
                cube.Lower[0] = cube.Left[:, 2]
                cube.Left[:, 2] = upper_prev[2, ::-1]

            elif face == "B":

                upper_prev = cube.Upper.copy()

                cube.Back = np.rot90(cube.Back, 1, (0, 1))

                cube.Upper[0] = cube.Left[::-1, 0]
                cube.Left[:, 0] = cube.Lower[2]
                cube.Lower[2] = cube.Right[::-1, 2]
                cube.Right[:, 2] = upper_prev[0]
