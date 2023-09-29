# CubeTutor

CubeTutor is an engaging Python program designed to bring the legendary Rubik's Cube to life in a vibrant 3D environment. Whether you're a beginner eager to learn the art of Rubik's Cube solving or an experienced enthusiast honing your skills, CubeTutor is here to guide you through the fascinating world of twisty puzzles.

## Features:

🔹 🔎 **Immersive 3D Experience:** Explore the Rubik's Cube in an immersive 3D space, allowing you to inspect the cube from every angle.
<div align="center">
  <img width="640" height="480" src="https://github.com/aepii/CubeTutor/assets/68669356/82954ee1-bf25-405e-a6dd-3048fd6fe796">
  
</div>

🔹 🔄 **Customizable Moves:** Input your move sequences and watch as the cube dynamically responds, providing visual feedback for your algorithm experiments.
<div align="center">
  <img width="640" height="480" src="https://github.com/aepii/CubeTutor/assets/68669356/fab969f2-9609-4a7e-a537-46d40e7ff9cd">
  
</div>

## Future Enhancements:

🔹 🚀 **Real-Time Cube Scanning with OpenCV:** CubeTutor is gearing up for a major upgrade! In the future, you can expect the integration of OpenCV, enabling the program to capture your physical Rubik's Cube directly into the virtual environment. Watch as your real-world moves translate into the digital realm!

🔹 🔍 **Algorithm Suggestions at Your Fingertips:** CubeTutor gets even smarter! By scanning specific PLL (Permutation of the Last Layer) or OLL (Orientation of the Last Layer) configurations, CubeTutor will tap into its extensive database. It will then fetch and present you with a curated selection of algorithms sourced from leading cube algorithm websites. These algorithms will be tailored to your current cube state, providing you with multiple solving options.

*CubeTutor is not just a tutor; it's your personal Rubik's Cube mentor, continuously evolving to provide you with the best learning and solving experience possible.* 🌟🧩

**This project is W.I.P. and is mostly a mock-up.**

# Documentation

## Cube Class

The `Cube` class represents a Rubik's Cube. Each face of the cube is represented by a 3x3 matrix where the center value indicates the solved color. The matrix contains values from 0 to 5 representing different colors. Here's how the cube is structured:

- Front (F): Green (0)
- Back (B): Blue (1)
- Left (L): Orange (2)
- Right (R): Red (3)
- Upper (U): White (4)
- Lower (D): Yellow (5)

**Example: Front Face**
`[['0' '0' '0']
 ['0' '0' '0']
 ['0' '0' '0']]`

**Example: Scrambled Back Face**
`[['1' '3' '4']
 ['5' '1' '5']
 ['3' '2' '0']]`

## CubeBuilder Class

The `CubeBuilder` class facilitates the construction of a `Cube` object with customizable face configurations.

### Class Attributes:

- **Cube**: A `Cube` object to be built or modified.

### Class Methods:

#### `__init__(self, default=False)`

Initializes a `CubeBuilder` object.

- **Parameters:**
  - `default` (optional): If True, initializes the `CubeBuilder` with default face configurations. Defaults to False.


## CubeMoves Class

Typical Rubik's Cube notation follows:
- `F` : Front face is rotated clockwise
- `B` : Back face is rotated clockwise
- `L` : Left face is rotated clockwise
- `R` : Right face is rotated clockwise
- `U` : Upper Face is rotated clockwise
- `D` : Lower face is rotated clockwise

Notations can have prefixes where:
- ` ` : Face is rotated clockwise.
- `2` : Face is rotated 180 degrees.
- `'` : Face is rotated counterclockwise.
- `2'` : Face is rotated 180 degrees counterclockwise. *this is mainly used for finger tricks.

### Methods

#### `add_moves(self, moves: str)`

Adds moves to the deque. Parses input string to handle multiple moves.

- `moves` (str): A string representing the moves, separated by spaces.
  Example: `moves = "F2 B' U2' U L R D' R2"`

#### `execute_moves(self, cube: Cube, solve: bool = True)`

Executes the moves on the provided Cube object.

- `cube` (Cube): The Cube object on which moves will be executed.
- `solve` (bool, optional): If True, executes moves until the deque is empty, else executes a single move.

#### `_perform_move(self, cube: Cube, move: str)`

Performs a single move on the provided Cube object.

- `cube` (Cube): The Cube object on which the move will be performed.
- `move` (str): The move to be executed.
  Example: `move = "F2"`

#### `_rotate_cube(cube: Cube, face: str, clockwise: bool = True, double: bool = False)`

Rotates the cube's face either clockwise, counterclockwise, or 180 degrees based on input parameters.

- `cube` (Cube): The Cube object on which the rotation will be performed.
- `face` (str): The face of the cube to be rotated.
- `clockwise` (bool, optional): If True, rotates the face clockwise. If False, rotates counterclockwise.
- `double` (bool, optional): If True, rotates the face by 180 degrees.

## `CubeRender` Class

The `CubeRender` class is responsible for rendering a 3D Rubik's Cube using Matplotlib.

### Attributes:

- **cube**: A `Cube` object representing the Rubik's Cube to be rendered.
- **faces**: A list to store the generated 3D coordinates of the cube's faces.
- **plane_map**: A mapping of face names to indicators for generating 3D coordinates of Rubik's Cube facelets.
- **fig**: A Matplotlib figure for 3D rendering.
- **ax**: A Matplotlib axis for the 3D plot.

### Methods:

#### `_generate_point(indicator, scope) -> np.ndarray`

Generates a 3D point based on the indicator value and the scope of the facelet.

- **Parameters:**
  - `indicator`: Indicator value for the axis (0, 3, -1, or -2).
  - `scope`: Range of values for the facelet (i, j).
- **Returns:**
  - A 3D point represented as a NumPy array.

#### `_get_color(self, x, y, z, count) -> str`

Determines the color of a facelet based on its position and cube configuration.

- **Parameters:**
  - `x, y, z`: 3D coordinates of the facelet.
  - `count`: Position of the facelet in the sequence.
- **Returns:**
  - A string representing the color of the facelet.

#### `_create_plane(self, face)`

Creates a 3x3 plane (face) with the specified color.

- **Parameters:**
  - `face`: Face ('Front', 'Back', 'Left', 'Right', 'Upper', or 'Lower').

#### `render(self)`

Renders the Rubik's Cube in 3D using Matplotlib.

## Usage Example:

<div align="center">
  <img width="640" height="480" src="https://github.com/aepii/CubeTutor/assets/68669356/f0266268-1fa2-4f22-8972-32cd06908fae">
  
</div>

```python
from cube_modules.cube import CubeBuilder
from cube_modules.cube_moves import CubeMoves
from cube_modules.cube_render import CubeRender

myCube = CubeBuilder(default=True)

moves = CubeMoves().add_moves("R F2 D'")
moves.execute_moves(myCube.Cube)

render = CubeRender(myCube.Cube)
render.render()
```


       

