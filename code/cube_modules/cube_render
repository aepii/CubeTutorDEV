import matplotlib.pyplot as plt
import numpy as np


class CubeRender:
    """
        A class for rendering a 3D Rubik's Cube using Matplotlib.
    """

    def __init__(self, cube):
        """
            Initializes the CubeRender object.

            Args:
            - cube_modules: A Cube object representing the Rubik's Cube to be rendered.
        """
        self.cube = cube
        self.faces = []

        # Mapping of face names to indicators for generating 3D coordinates of Rubik's Cube facelets.
        """
            Values: 
            - 0 and 3: Represents a constant coordinate value of [[0]] or [[3]] respectively.
            - -1: Indicates the coordinate relies on [[i], [i + 1]], where i is the row index.
            - -2: Indicates the coordinate relies on [[j, j + 1]], where j is the column index.
        """
        self.plane_map = {'Front': [3, -2, -1], 'Back': [0, -2, -1], 'Left': [-2, 0, -1],
                          'Right': [-2, 3, -1], 'Upper': [-1, -2, 3], 'Lower': [-1, -2, 0]}

        # Initialize a 3D plot for rendering the cube_modules.
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.view_init(elev=15, azim=45)

        # Set titles for the plot.
        plt.title(label=f'Cube Object: {id(self.cube)}', fontstyle='normal', horizontalalignment='center')
        plt.suptitle(f'3D Render', fontstyle='italic', horizontalalignment='center')
        self.ax.text2D(0.5, 0.95, f'Moves: {" ".join(self.cube.history)}', transform=self.ax.transAxes,
                       horizontalalignment='center', verticalalignment='center')

        plt.grid(False)
        plt.axis('off')

    def render(self):
        """
            Renders the Rubik's Cube in 3D using Matplotlib.
        """
        # Create planes for the cube_modules.
        for face in self.plane_map.keys():
            self._create_plane(face)

        # Plot the surfaces of the cube_modules faces.
        for face in self.faces:
            for facelet in face:
                self.ax.plot_surface(facelet[0], facelet[1], facelet[2], color=facelet[3], linewidth=1,
                                     edgecolors='black', shade=False)

        # Set up the dimensions of the 3D plot.
        axes = [3, 3, 3]
        data = np.ones(axes, dtype=bool)

        # Display the 3D plot.
        plt.draw()
        plt.show()

    @staticmethod
    def _generate_point(indicator, scope):
        """
            Generates a 3D point based on the indicator value and the scope of the facelet.

            Args:
            - indicator: Indicator value for the axis (0, 3, -1, or -2).
            - scope: Range of values for the facelet (i, j).

            Returns:
            A 3D point represented as a NumPy array.
        """
        i, j = scope[0], scope[1]
        if indicator == 0 or indicator == 3:
            return np.array([[indicator]])
        elif indicator == -1:
            return np.array([[i], [i + 1]])
        elif indicator == -2:
            return np.array([[j, j + 1]])

    def _get_color(self, x, y, z, count):
        """
            Determines the color of a facelet based on its position and cube_modules configuration.

            Args:
            - x, y, z: 3D coordinates of the facelet.
            - count: Position of the facelet in the sequence.

            Returns:
            A string representing the color of the facelet.
        """
        # Mapping of numeric values to corresponding colors.
        value_to_color = {
            0: "g",  # Green
            1: "b",  # Blue
            2: "#FFA500",  # Orange
            3: "r",  # Red
            4: "w",  # White
            5: "y"  # Yellow
        }

        # Determine the color based on the facelet's position.
        if np.array_equal(x, [[3]]):
            color = value_to_color[self.cube.getFront()[2 - (count - 1) // 3][(count - 1) % 3]]
        elif np.array_equal(x, [[0]]):
            color = value_to_color[self.cube.getBack()[2 - (count - 1) // 3][(9 - count) % 3]]
        elif np.array_equal(y, [[0]]):
            color = value_to_color[self.cube.getLeft()[2 - (count - 1) // 3][(count - 1) % 3]]
        elif np.array_equal(y, [[3]]):
            color = value_to_color[self.cube.getRight()[2 - (count - 1) // 3][(9 - count) % 3]]
        elif np.array_equal(z, [[3]]):
            color = value_to_color[self.cube.getUpper()[(count - 1) // 3][(count - 1) % 3]]
        elif np.array_equal(z, [[0]]):
            color = value_to_color[self.cube.getLower()[2 - (count - 1) // 3][(count - 1) % 3]]
        else:
            color = 'k'  # Black for unrecognized facelets.

        return color

    def _create_plane(self, face):
        """
            Creates a 3x3 plane (face) with the specified color.

            Args:
            - face: Face ('Front', 'Back', 'Left', 'Right', 'Upper', or 'Lower').
        """
        plane_map = self.plane_map[face]
        plane = []

        count = 0
        # Generate 3x3 facelets for the specified face.
        for i in range(0, 3):
            for j in range(0, 3):
                count += 1
                x = self._generate_point(plane_map[0], [i, j])
                y = self._generate_point(plane_map[1], [i, j])
                z = self._generate_point(plane_map[2], [i, j])

                # Determine the color of the facelet based on its position and count.
                plane.append([x, y, z, self._get_color(x, y, z, count)])

        # Add the generated face to the list of faces.
        self.faces.append(plane)
