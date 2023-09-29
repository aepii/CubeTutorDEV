from .cube import CubeBuilder
from .cube_moves import CubeMoves
from .cube_render import CubeRender


class Application:
    def __init__(self):
        self.data = {
            'cubes': {},
            'move_sequences': {}
        }

    def run(self):

        print("Welcome To Cube Tutor!")

        self._front_end()

    def _front_end(self):
        print("\nCommands:\n1) Create A Cube\n2) Add A Move Sequence\n3) Execute Move "
              "Sequence\n4) List All Cubes\n5) List All Move Sequences\n6) Color Visualization\n7) Render Cube"
              "\n8) Exit")

        command = int(input("Enter A Command: "))

        # Create A Cube
        if command == 1:

            cube_name = input("Enter A Cube Name: ")
            cube = CubeBuilder(default=True)
            self.data['cubes'][cube_name] = cube

            return self._front_end()

        # Add A Move Sequence To A Cube
        elif command == 2:

            print("Valid Moves Are: F, B, L, R, U, D (Valid Suffixes: , 2, ')")
            move_sequence = input("Enter A Move Sequence: ")
            cube_name = input("Enter A Cube Name To Match The Move Sequence To: ")
            moves = CubeMoves().add_moves(move_sequence)
            self.data['move_sequences'][cube_name] = moves

            return self._front_end()

        # Execute A Cube's Move Sequences
        elif command == 3:

            cube_name = input("Enter A Cube Name: ")
            self.data['move_sequences'][cube_name].execute_moves(self.data['cubes'][cube_name].Cube)
            del self.data['move_sequences'][cube_name]

            return self._front_end()

        elif command == 4:

            for cube_name, cube in self.data['cubes'].items():
                print(f"{cube_name}: {cube.Cube.history}")

            return self._front_end()

        elif command == 5:

            for cube_name, moves in self.data['move_sequences'].items():
                print(f"{cube_name}: {moves.moves}")

            return self._front_end()

        elif command == 6:

            cube_name = input("Enter A Cube Name: ")
            print(self.data['cubes'][cube_name].Cube.color_visualization())

            return self._front_end()

        # Render The Cube
        elif command == 7:

            cube_name = input("Enter A Cube Name To Render: ")
            newRender = CubeRender(self.data['cubes'][cube_name].Cube)

            newRender.render()

            return self._front_end()

        elif command == 8:
            print('Exiting')
