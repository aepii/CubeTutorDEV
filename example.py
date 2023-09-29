from cube_modules.cube import CubeBuilder
from cube_modules.cube_moves import CubeMoves
from cube_modules.cube_render import CubeRender

myCube = CubeBuilder(default=True)

moves = CubeMoves().add_moves("R F2 D'")
moves.execute_moves(myCube.Cube)

render = CubeRender(myCube.Cube)
render.render()
