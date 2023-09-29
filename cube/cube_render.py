import matplotlib.pyplot as plt
import numpy as np


class CubeRender:

    def __init__(self):

        self.faces = []
        self.face_map = {'g': [3, -2, -1], 'b': [0, -2, -1], 'o': [-2, 0, -1], 'r': [-2, 3, -1], 'w': [-1, -2, 3],
                         'y': [-1, -2, 0]}

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.view_init(elev=30, azim=45)
        plt.title(label="3D Render", loc="center", fontstyle='normal')
        plt.suptitle('Subtitle', fontstyle='italic')
        self.ax.text2D(0.05, 0.95, '0 moves', transform=self.ax.transAxes, fontstyle='italic', color='grey')

    def render(self):

        for face in self.face_map.keys():
            print(face)
            self.create_face(face)

        for face in self.faces:
            for facelet in face:
                self.ax.plot_surface(facelet[0], facelet[1], facelet[2], color=facelet[3], linewidth=1,
                                     edgecolors='black', shade=False)

        axes = [3, 3, 3]
        data = np.ones(axes, dtype=bool)

        plt.show()

    def create_face(self, color):

        map = self.face_map[color]
        face = []
        for i in range(0, 3):
            for j in range(0, 3):
                x = self.generate_point(map[0], [i, j])
                y = self.generate_point(map[1], [i, j])
                z = self.generate_point(map[2], [i, j])

                face.append([x, y, z, self.get_color(x, y, z)])
                print("Point: ", x, y, z)

        self.faces.append(face)

    @staticmethod
    def get_color(x, y, z):

        if np.array_equal(x, [[3]]):  # Front Face
            color = 'g'
        elif np.array_equal(x, [[0]]):
            color = 'b'
        elif np.array_equal(y, [[0]]):
            color = '#FFA500'
        elif np.array_equal(y, [[3]]):
            color = 'r'
        elif np.array_equal(z, [[3]]):
            color = 'w'
        elif np.array_equal(z, [[0]]):
            color = 'y'
        else:
            color = 'w'

        return color

    @staticmethod
    def generate_point(constant, range):
        i, j = range[0], range[1]

        if constant == 0 or constant == 3:
            return np.array([[constant]])
        elif constant == -1:
            return np.array([[i], [i + 1]])
        elif constant == -2:
            return np.array([[j, j + 1]])
