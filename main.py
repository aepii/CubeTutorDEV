from cube.cube import CubeBuilder
from cube.cube_moves import CubeMoves

from cube.cube_render import CubeRender

import numpy as np
import cv2


def main():
    cube1 = CubeBuilder() \
        .updateFront([[2, 1, 1], [0, 0, 1], [5, 2, 0]]) \
        .updateBack() \
        .updateLeft() \
        .updateRight() \
        .updateUpper() \
        .updateLower()

    cube1.updateFront()

    cube2 = CubeBuilder(default=True)

    print(cube1.Cube)
    print(cube2.Cube)

    print(cube2.Cube.color_visualization())

    cubeMoves = CubeMoves().add_moves("L' B2 D' F R2 L' F2 D R D2 F2'")

    cubeMoves.execute_moves(cube2.Cube)

    print(cube2.Cube)

    print(cube2.Cube.color_visualization())

    print(cubeMoves.history, cubeMoves.moves)

    newRender = CubeRender(cube2.Cube)
    newRender.render()


if __name__ == "__main__":
    main()
