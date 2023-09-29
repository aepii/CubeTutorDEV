import numpy as np


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

    # Initialize a Cube Object with all faces set to None.
    def __init__(self):

        """
            Attributes:
            - history: A list to store the history of moves made on the cube.
            - Front, Back, Left, Right, Upper, Lower: 3x3 matrices representing the cube faces.
        """

        self.history = []

        self.Front = None
        self.Back = None
        self.Left = None
        self.Right = None
        self.Upper = None
        self.Lower = None

    # Sets the front face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setFront(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Front = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        else:
            self.Front = np.array(entry)

    # Sets the back face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setBack(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Back = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        else:
            self.Back = np.array(entry)

    # Sets the left face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setLeft(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Left = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        else:
            self.Left = np.array(entry)

    # Sets the right face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setRight(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Right = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
        else:
            self.Right = np.array(entry)

    # Sets the upper face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setUpper(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Upper = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
        else:
            self.Upper = np.array(entry)

    # Sets the lower face of a Cube to a given matrix. Otherwise, defaults to a specific matrix if None is provided.
    def setLower(self, entry=None):
        """
            Args:
            - entry (optional): A 3x3 matrix representing the front face. Defaults to a solved state if None.
        """
        if entry is None:
            self.Lower = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
        else:
            self.Lower = np.array(entry)

    # Gets the front face of a Cube. Returns a matrix.
    def getFront(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Front

    # Gets the back face of a Cube. Returns a matrix.
    def getBack(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Back

    # Gets the left face of a Cube. Returns a matrix.
    def getLeft(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Left

    # Gets the right face of a Cube. Returns a matrix.
    def getRight(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Right

    # Gets the upper face of a Cube. Returns a matrix.
    def getUpper(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Upper

    # Gets the lower face of a Cube. Returns a matrix.
    def getLower(self):
        """
            Returns:
            A 3x3 matrix representing the front face.
        """
        return self.Lower

    # Returns a printable representation of a Cube.
    def __repr__(self):
        """
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

    # Returns a printable representation of a Cube with colors representing each entry.
    def color_visualization(self):
        """
            Returns:
            A string representing the Cube object including its memory address and colors indicating the face configurations.
        """
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

        result = f"Cube Object: {id(self)}\n"

        for face, matrix in faces.items():
            colors = np.array([[value_to_color[val] for val in row] for row in matrix])
            result += f"{face}:\n{colors}\n"

        return result


class CubeBuilder:
    """
        A CubeBuilder object facilitates the construction of a Cube object with customizable face configurations.
    """
    def __init__(self, default=False):

        """
            Initializes a CubeBuilder object.

            Args:
            - default (optional): If True, initializes the CubeBuilder with default face configurations. Defaults to False.

            Attributes:
            - Cube: A Cube object to be built or modified.
        """

        self.Cube = Cube()
        if default:
            self.updateFront() \
                .updateBack() \
                .updateLeft() \
                .updateRight() \
                .updateUpper() \
                .updateLower()

    # Updates the front face of the Cube.
    def updateFront(self, entry=None):
        """
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

    # Updates the back face of the Cube.
    def updateBack(self, entry=None):
        """
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

    # Updates the left face of the Cube.
    def updateLeft(self, entry=None):
        """
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

    # Updates the right face of the Cube.
    def updateRight(self, entry=None):
        """
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

    # Updates the upper face of the Cube.
    def updateUpper(self, entry=None):
        """
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

    # Updates the lower face of the Cube.
    def updateLower(self, entry=None):
        """
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
