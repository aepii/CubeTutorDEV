from cube.cube import CubeBuilder
from cube.cube_moves import CubeMoves

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

    cubeMoves = CubeMoves().add_move("F").add_move("U").add_move("D").add_move("B").add_move("D").add_move(
        "R").add_move("L").add_move("U").add_move("F").add_move("R")

    print(cubeMoves.moves)

    cubeMoves.execute_moves(cube2.Cube)

    print(cube2.Cube)

    print(cube2.Cube.color_visualization())


if __name__ == "__main__":
    main()
