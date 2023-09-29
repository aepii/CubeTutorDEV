# CubeTutor

CubeTutor is an engaging Python program designed to bring the legendary Rubik's Cube to life in a vibrant 3D environment. Whether you're a beginner eager to learn the art of Rubik's Cube solving or an experienced enthusiast honing your skills, CubeTutor is here to guide you through the fascinating world of twisty puzzles.

## Features:

🔹 🔎 **Immersive 3D Experience:** Explore the Rubik's Cube in an immersive 3D space, allowing you to inspect the cube from every angle.
<div align="center">
  <img width="649" height="480" src="https://github.com/aepii/CubeTutor/assets/68669356/82954ee1-bf25-405e-a6dd-3048fd6fe796">
  
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

## DOCUMENTATION:

### **Cube**

    A Rubik's Cube is represented by six faces:
      - Front (F): Green (0)
      - Back (B): Blue (1)
      - Left (L): Orange (2)
      - Right (R): Red (3)
      - Upper (U): White (4)
      - Lower (D): Yellow (5)

    Official scramble orientation is green in front and white on top, hence the values above.

    Values ranging from 0 to 5 are used instead of colors to support different colored cubes.
  
    Each face is a 3x3 matrix with entries ranging from 0 to 5.
  
    Face = [ [*,*,*], [*,x,*], [*,*,*] ]
  
    The center value (x in the matrix) represents the solved color of the face, with an entry ranging from 0 to 5.
    The * represents entries ranging from 0 to 5 for the remaining elements in the matrix.

### **Cube Moves**
    
    Typical Rubik's Cube notation follows:
      - F : Front face is rotated clockwise
      - B : Back face is rotated clockwise
      - L : Left face is rotated clockwise
      - R : Right face is rotated clockwise
      - U : Upper Face is rotated clockwise
      - D : Lower face is rotated clockwise
  
    Notations can have prefixes where:
      - 2 : Face is rotated 180 degrees.
      - ' : Face is rotated counterclockwise.
      - 2' : Face is rotated 180 degrees counterclockwise. *this is mainly used for finger tricks.

**Methods:**

```python


add_moves(self, moves) #Adds moves to the deque. Parses input string to handle multiple moves.
  moves (str): #A string representing the moves. Can include space-separated moves.
    example : #moves = "F2 B' U2' U L R D' R2"
  
execute_moves(self, cube, solve=True) #Executes the moves on the provided Cube object.
  cube_modules (Cube): #The Cube object on which moves will be executed.
  solve (bool): #If True, executes moves until the deque is empty, else executes a single move.

_perform_move(self, cube, move) #Performs a single move on the provided Cube object.
  cube_modules (Cube): #The Cube object on which the move will be performed.
  move (str): #The move to be executed.
    example : #move = "F2"
    
_rotate_cube(cube, face, clockwise=True, double=False) #Rotates the cube_modules's face either clockwise, counterclockwise, or 180 degrees based on input parameters.
    cube (Cube): #The Cube object on which the rotation will be performed.
    face (str): #The face of the cube_modules to be rotated.
    clockwise (bool): #If True, rotates the face clockwise. If False, rotates counterclockwise.
    double (bool): #If True, rotates the face by 180 degrees.
```

       

