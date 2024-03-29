import numpy as np
from .cube_moves import CubeMoves


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

        Each face is a 3x3 matrix with entries ranging from 0 to 5.

        Face = [ [*,*,*], [*,x,*], [*,*,*] ]

        The center value (x in the matrix) represents the solved color of the face, with an entry ranging from 0 to 5.
        The * represents entries ranging from 0 to 5 for the remaining elements in the matrix.
    """

    def __init__(self):

        """
            Initialize a Cube Object with all faces set to None.

            Attributes:
            - history: A list to store the history of moves made on the cube_modules.
            - Front, Back, Left, Right, Upper, Lower: 3x3 matrices representing the cube_modules faces.
        """

        self.history = []

        self.Front = None
        self.Back = None
        self.Left = None
        self.Right = None
        self.Upper = None
        self.Lower = None

    def setFront(self, entry=None):
        """
            Sets the front face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Front = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        else:
            self.Front = np.array(entry)

    def setBack(self, entry=None):
        """
            Sets the back face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Back = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        else:
            self.Back = np.array(entry)

    def setLeft(self, entry=None):
        """
            Sets the left face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Left = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        else:
            self.Left = np.array(entry)

    def setRight(self, entry=None):
        """
            Sets the right face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Right = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
        else:
            self.Right = np.array(entry)

    def setUpper(self, entry=None):
        """
            Sets the upper face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Upper = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
        else:
            self.Upper = np.array(entry)

    def setLower(self, entry=None):
        """
            Sets the lower face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.

            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Lower = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
        else:
            self.Lower = np.array(entry)

    def getFront(self):
        """
            Gets the front face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Front

    def getBack(self):
        """
            Gets the back face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Back

    def getLeft(self):
        """
            Gets the left face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Left

    def getRight(self):
        """
            Gets the right face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Right

    def getUpper(self):
        """
            Gets the upper face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Upper

    def getLower(self):
        """
            Gets the lower face of a Cube. Returns a matrix.

            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Lower

    def __repr__(self):
        """
            Returns a printable representation of a Cube.

            Returns:
            A string representing the Cube object including its memory address and face configurations.
        """
        return (f"Cube Object: {id(self)}\n"
                f"Front:\n{self.Front}\n"
                f"Back:\n{self.Back}\n"
                f"Left:\n{self.Left}\n"
                f"Right:\n{self.Right}\n"
                f"Up:\n{self.Upper}\n"
                f"Down:\n{self.Lower}"
                )

    def color_visualization(self):
        """
            Returns a printable representation of a Cube with colors representing each entry.

            Returns:
            A string representing the Cube object including its memory address and colors indicating the face configurations.
        """
        value_to_color = {
            0: "Green",
            1: "Blue",
            2: "Orange",
            3: "Red",
            4: "White",
            5: "Yellow",
            6: "Grey"
        }

        faces = {
            'Front': self.Front,
            'Back': self.Back,
            'Left': self.Left,
            'Right': self.Right,
            'Up': self.Upper,
            'Down': self.Lower
        }

        result = f"Cube Object: {id(self)}\n"

        for face, matrix in faces.items():
            colors = np.array([[value_to_color[val] for val in row] for row in matrix])
            result += f"{face}:\n{colors}\n"

        return result


class CubeBuilder:
    """
        A CubeBuilder object facilitates the construction of a Cube object with customizable face configurations.
    """

    def __init__(self, move_sequence=None, data_base_build=None):

        """
            Initializes a CubeBuilder object.

            Args:
            - default (optional): If True, initializes the CubeBuilder with default face configurations. Defaults to False.

            Attributes:
            - Cube: A Cube object to be built or modified.
        """

        self.Cube = Cube()
        self.updateFront() \
            .updateBack() \
            .updateLeft() \
            .updateRight() \
            .updateUpper() \
            .updateLower()

        if move_sequence:
            cubeMoves = CubeMoves()
            cubeMoves.add_moves(move_sequence)
            cubeMoves.execute_moves(self.Cube)
        elif data_base_build:
            self.buildFromDataBase(data_base_build)

    def updateFront(self, entry=None):
        """
            Updates the front face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new front face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setFront(entry)
        else:
            self.Cube.setFront()
        return self

    def updateBack(self, entry=None):
        """
            Updates the back face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new back face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setBack(entry)
        else:
            self.Cube.setBack()
        return self

    def updateLeft(self, entry=None):
        """
            Updates the left face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new left face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setLeft(entry)
        else:
            self.Cube.setLeft()
        return self

    def updateRight(self, entry=None):
        """
            Updates the right face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new right face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setRight(entry)
        else:
            self.Cube.setRight()
        return self

    def updateUpper(self, entry=None):
        """
            Updates the upper face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new upper face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setUpper(entry)
        else:
            self.Cube.setUpper()
        return self

    def updateLower(self, entry=None):
        """
            Updates the lower face of the Cube.

            Args:
            - entry (optional): A 3x3 matrix representing the new lower face. Defaults to a solved state if None.

            Returns:
            The CubeBuilder object for method chaining.
        """
        if entry is not None:
            self.Cube.setLower(entry)
        else:
            self.Cube.setLower()
        return self

    def buildFromDataBase(self, colors):

        face_map = {
            'g': [0, self.updateFront],  # Green
            'b': [1, self.updateBack],   # Blue
            'o': [2, self.updateRight],  # Orange
            'r': [3, self.updateLeft],   # Red
            'w': [4, self.updateLower],  # White
            'y': [5, self.updateUpper],  # Yellow
            'l': [6, self.updateUpper]   # Grey
        }

        for face_index in range(5):
            center_piece = colors[4 + (face_index * 9)]
            update_function = face_map[center_piece][1]
            facelet_colors = colors[face_index * 9: (face_index + 1) * 9]
            facelet_indices = [[face_map[color][0] for color in facelet_colors[i:i + 3]] for i in range(0, 9, 3)]
            update_function(facelet_indices)
