from cube.cube import CubeBuilder
from cube.cube_moves import CubeMoves
from cube.cube_render import CubeRender


def main():
    myCube = CubeBuilder(default=True)

    print(myCube.Cube.color_visualization())

    cubeMoves = CubeMoves().add_moves("L' B2 D' F R2 L' F2 D R D2 F2'")

    cubeMoves.execute_moves(myCube.Cube)

    print(myCube.Cube.color_visualization())

    print(myCube.Cube.history, cubeMoves.moves)

    newRender = CubeRender(myCube.Cube)
    newRender.render()


if __name__ == "__main__":
    main()
