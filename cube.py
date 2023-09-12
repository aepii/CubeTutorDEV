class Cube:
    """
        A standard Cube object is represented by six faces:
        - Front (F): Green (0)
        - Back (B): Blue (1)
        - Left (L): Orange (2)
        - Right (R): Red (3)
        - Upper (U): White (4)
        - Lower (D): Yellow (5)

        Values ranging from 0 to 5 are used instead of colors to support different colored cubes.

        Each face is a 3x3 matrix with values ranging from 0 to 5.

        Face = [ [*,*,*], [*,x,*], [*,*,*] ]

        The center value (x in the matrix) represents the solved color of the face, with a value ranging from 0 to 5.
        The * represents values ranging from 0 to 5 for the remaining elements in the matrix.
    """

    # Initialize a Cube Object with all faces set to None.
    def __init__(self):
        self.Front = None
        self.Back = None
        self.Left = None
        self.Right = None
        self.Upper = None
        self.Lower = None

    # Sets the front face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setFront(self, entry=None):
        if entry is None:
            self.Front = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            self.Front = entry

    # Sets the back face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setBack(self, entry=None):
        if entry is None:
            self.Back = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        else:
            self.Back = entry

    # Sets the left face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setLeft(self, entry=None):
        if entry is None:
            self.Left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        else:
            self.Left = entry

    # Sets the right face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setRight(self, entry=None):
        if entry is None:
            self.Right = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        else:
            self.Right = entry

    # Sets the upper face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setUpper(self, entry=None):
        if entry is None:
            self.Upper = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        else:
            self.Upper = entry

    # Sets the lower face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setLower(self, entry=None):
        if entry is None:
            self.Lower = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        else:
            self.Lower = entry

    def getFront(self):
        return self.Front

    def getBack(self):
        return self.Back

    def getLeft(self):
        return self.Left

    def getRight(self):
        return self.Right

    def getUpper(self):
        return self.Upper

    def getLower(self):
        return self.Lower

    def __repr__(self):
        return (f"Cube Object\n"
                f"Front: {self.Front}\n"
                f"Back: {self.Back}\n"
                f"Left: {self.Left}\n"
                f"Right: {self.Right}\n"
                f"Up: {self.Upper}\n"
                f"Down: {self.Lower}"
                )

    def color_visualization(self):

        value_to_color = {
            0: "Green",
            1: "Blue",
            2: "Orange",
            3: "Red",
            4: "White",
            5: "Yellow"
        }

        faces = {
            'Front': self.Front,
            'Back': self.Back,
            'Left': self.Left,
            'Right': self.Right,
            'Up': self.Upper,
            'Down': self.Lower
        }

        result = f"Cube Object\n"
        for face, matrix in faces.items():
            colors = [[value_to_color[val] for val in row] for row in matrix]
            result += f"{face}: {colors}\n"

        return result


class CubeBuilder:
    def __init__(self, default=False):
        self.Cube = Cube()
        if default:
            self.updateFront()
            self.updateBack()
            self.updateLeft()
            self.updateRight()
            self.updateUpper()
            self.updateLower()

    def updateFront(self, entry=None):
        if entry is not None:
            self.Cube.setFront(entry)
        else:
            self.Cube.setFront()
        return self

    def updateBack(self, entry=None):
        if entry is not None:
            self.Cube.setBack(entry)
        else:
            self.Cube.setBack()
        return self

    def updateLeft(self, entry=None):
        if entry is not None:
            self.Cube.setLeft(entry)
        else:
            self.Cube.setLeft()
        return self

    def updateRight(self, entry=None):
        if entry is not None:
            self.Cube.setRight(entry)
        else:
            self.Cube.setRight()
        return self

    def updateUpper(self, entry=None):
        if entry is not None:
            self.Cube.setUpper(entry)
        else:
            self.Cube.setUpper()
        return self

    def updateLower(self, entry=None):
        if entry is not None:
            self.Cube.setLower(entry)
        else:
            self.Cube.setLower()
        return self


from collections import deque


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
    def _rotate_cube(cube, face, clockwise=False, double=False):

        if face == "U":
            front_prev = cube.getFront()
            left_prev = cube.getLeft()
            back_prev = cube.getBack()
            right_prev = cube.getRight()

            upper_prev = cube.getUpper()

            upper_cur = cube.setUpper([
                [upper_prev[2][0], upper_prev[1][0], upper_prev[0][0]],
                [upper_prev[2][1], upper_prev[1][1], upper_prev[0][1]],
                [upper_prev[2][2], upper_prev[1][2], upper_prev[0][2]]
            ])

            front_cur = cube.setFront([right_prev[0], front_prev[1], front_prev[2]])
            left_cur = cube.setLeft([front_prev[0], left_prev[1], left_prev[2]])
            back_cur = cube.setBack([left_prev[0], back_prev[1], back_prev[2]])
            right_cur = cube.setRight([back_prev[0], right_prev[1], right_prev[2]])

        elif face == "D":
            front_prev = cube.getFront()
            left_prev = cube.getLeft()
            back_prev = cube.getBack()
            right_prev = cube.getRight()

            lower_prev = cube.getLower()

            lower_cur = cube.setLower([
                [lower_prev[2][0], lower_prev[1][0], lower_prev[0][0]],
                [lower_prev[2][1], lower_prev[1][1], lower_prev[0][1]],
                [lower_prev[2][2], lower_prev[1][2], lower_prev[0][2]]
            ])

            front_cur = cube.setFront([front_prev[0], front_prev[1], left_prev[2]])
            left_cur = cube.setLeft([left_prev[0], left_prev[1], back_prev[2]])
            back_cur = cube.setBack([back_prev[0], back_prev[1], right_prev[2]])
            right_cur = cube.setRight([right_prev[0], right_prev[1], front_prev[2]])

        elif face == "L":
            front_prev = cube.getFront()
            lower_prev = cube.getLower()
            back_prev = cube.getBack()
            upper_prev = cube.getUpper()

            left_prev = cube.getLeft()

            left_cur = cube.setLeft([
                [left_prev[2][0], left_prev[1][0], left_prev[0][0]],
                [left_prev[2][1], left_prev[1][1], left_prev[0][1]],
                [left_prev[2][2], left_prev[1][2], left_prev[0][2]]
            ])

            front_cur = cube.setFront([
                [upper_prev[0][0], front_prev[0][1], front_prev[0][2]],
                [upper_prev[1][0], front_prev[1][1], front_prev[1][2]],
                [upper_prev[2][0], front_prev[2][1], front_prev[2][2]]
            ])

            lower_cur = cube.setLower([
                [front_prev[0][0], lower_prev[0][1], lower_prev[0][2]],
                [front_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                [front_prev[2][0], lower_prev[2][1], lower_prev[2][2]]
            ])

            back_cur = cube.setBack([
                [back_prev[0][0], back_prev[0][1], lower_prev[2][0]],
                [back_prev[1][0], back_prev[1][1], lower_prev[1][0]],
                [back_prev[2][0], back_prev[2][1], lower_prev[0][0]]
            ])

            upper_cur = cube.setUpper([
                [back_prev[2][2], upper_prev[0][1], upper_prev[0][2]],
                [back_prev[1][2], upper_prev[1][1], upper_prev[1][2]],
                [back_prev[0][2], upper_prev[2][1], upper_prev[2][2]]
            ])

        elif face == "R":
            front_prev = cube.getFront()
            lower_prev = cube.getLower()
            back_prev = cube.getBack()
            upper_prev = cube.getUpper()

            right_prev = cube.getRight()

            right_cur = cube.setRight([
                [right_prev[2][0], right_prev[1][0], right_prev[0][0]],
                [right_prev[2][1], right_prev[1][1], right_prev[0][1]],
                [right_prev[2][2], right_prev[1][2], right_prev[0][2]]
            ])

            front_cur = cube.setFront([
                [front_prev[0][0], front_prev[0][1], lower_prev[0][2]],
                [front_prev[1][0], front_prev[1][1], lower_prev[1][2]],
                [front_prev[2][0], front_prev[2][1], lower_prev[2][2]]
            ])

            lower_cur = cube.setLower([
                [lower_prev[0][0], lower_prev[0][1], back_prev[2][0]],
                [lower_prev[1][0], lower_prev[1][1], back_prev[1][0]],
                [lower_prev[2][0], lower_prev[2][1], back_prev[0][0]]
            ])

            back_cur = cube.setBack([
                [upper_prev[2][2], back_prev[0][1], back_prev[0][2]],
                [upper_prev[1][2], back_prev[1][1], back_prev[1][2]],
                [upper_prev[0][2], back_prev[2][1], back_prev[2][2]]
            ])

            upper_cur = cube.setUpper([
                [upper_prev[0][0], upper_prev[0][1], front_prev[0][2]],
                [upper_prev[1][0], upper_prev[1][1], front_prev[1][2]],
                [upper_prev[2][0], upper_prev[2][1], front_prev[2][2]]
            ])

        elif face == "F":
            left_prev = cube.getLeft()
            lower_prev = cube.getLower()
            right_prev = cube.getRight()
            upper_prev = cube.getUpper()

            front_prev = cube.getFront()

            front_cur = cube.setFront([
                [front_prev[2][0], front_prev[1][0], front_prev[0][0]],
                [front_prev[2][1], front_prev[1][1], front_prev[0][1]],
                [front_prev[2][2], front_prev[1][2], front_prev[0][2]]
            ])

            left_cur = cube.setLeft([
                [left_prev[0][0], left_prev[0][1], lower_prev[0][0]],
                [left_prev[1][0], left_prev[1][1], lower_prev[0][1]],
                [left_prev[2][0], left_prev[2][1], lower_prev[0][2]]
            ])

            upper_cur = cube.setUpper([
                [upper_prev[0][0], upper_prev[0][1], upper_prev[0][2]],
                [upper_prev[1][0], upper_prev[1][1], upper_prev[1][2]],
                [left_prev[2][2], left_prev[1][2], left_prev[0][2]]
            ])

            right_cur = cube.setRight([
                [upper_prev[2][0], right_prev[0][1], right_prev[0][2]],
                [upper_prev[2][1], right_prev[1][1], right_prev[1][2]],
                [upper_prev[2][2], right_prev[2][1], right_prev[2][2]]
            ])

            lower_cur = cube.setLower([
                [right_prev[2][0], right_prev[1][0], right_prev[0][0]],
                [lower_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                [lower_prev[2][0], lower_prev[2][1], lower_prev[2][2]]
            ])

        elif face == "B":
            left_prev = cube.getLeft()
            lower_prev = cube.getLower()
            right_prev = cube.getRight()
            upper_prev = cube.getUpper()

            back_prev = cube.getBack()

            back_cur = cube.setBack([
                [back_prev[2][0], back_prev[1][0], back_prev[0][0]],
                [back_prev[2][1], back_prev[1][1], back_prev[0][1]],
                [back_prev[2][2], back_prev[1][2], back_prev[0][2]]
            ])

            left_cur = cube.setLeft([
                [upper_prev[0][2], left_prev[0][1], left_prev[0][2]],
                [upper_prev[0][1], left_prev[1][1], left_prev[1][2]],
                [upper_prev[0][0], left_prev[2][1], left_prev[2][2]]
            ])

            upper_cur = cube.setUpper([
                [right_prev[0][2], right_prev[1][2], right_prev[2][2]],
                [upper_prev[1][0], upper_prev[1][1], upper_prev[1][2]],
                [upper_prev[2][0], upper_prev[2][1], upper_prev[2][2]]
            ])

            right_cur = cube.setRight([
                [right_prev[0][0], right_prev[0][1], lower_prev[2][2]],
                [right_prev[1][0], right_prev[1][1], lower_prev[2][1]],
                [right_prev[2][0], right_prev[2][1], lower_prev[2][0]]
            ])

            lower_cur = cube.setLower([
                [lower_prev[0][0], lower_prev[0][1], lower_prev[0][2]],
                [lower_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                [left_prev[0][0], left_prev[1][0], left_prev[2][0]]
            ])
