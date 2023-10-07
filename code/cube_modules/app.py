from .cube import CubeBuilder
from .cube_moves import CubeMoves
from .cube_renderer import CubeRenderer


class Application:
    def __init__(self, MplCanvas):

        self.data = {
            'cubes': {},
            'move_sequences': {}
        }

        self.data['cubes']['Default'] = CubeBuilder()
        self.cube = 'Default'
        self.renderer = CubeRenderer(MplCanvas, self.data['cubes'][self.cube].Cube)
        self.renderer.render()

        print("Welcome To Cube Tutor!")

    def run(self):

        self._front_end()

    def _front_end(self):
        parse = input("[CubeTutor]: ")

        try:
            command, arguments = parse.split(" ", 1)
        except ValueError:
            command, arguments = parse, None

        command_map = {
            "lr": self._list_current_rendered_cube,
            "rn": self._render_cube,
            "c": self._create_cube,
            "cm": self._create_move_sequence,
            "ls": self._list_cubes,
            "lm": self._list_move_sequence,
            "ex": self._execute_move_sequence
        }

        if command in command_map:
            command_function = command_map[command]
            command_function(arguments)
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

    def _list_current_rendered_cube(self, arguments=None):
        print(self.cube, self.renderer.cube.history)

    def _create_cube(self, arguments):
        """
        Create Cube
        -c {cube_name} {o/move_sequence}
        """

        if arguments:

            args = arguments.split(" ", 1)
            cube_name = args[0] if len(args) > 0 else None
            move_sequence = args[1] if len(args) > 1 else None

            if len(args) < 1:
                print("Invalid input format. Usage: c {cube_name} {(optional) move_sequence}")
            else:
                if move_sequence:
                    cube = CubeBuilder(move_sequence)
                else:
                    cube = CubeBuilder()

                self.data['cubes'][cube_name] = cube
        else:
            print("Invalid input format. Usage: c {cube_name} {(optional) move_sequence}")

    def _create_move_sequence(self, arguments=None):
        """
        Create Move Sequence
        -cm {sequence_name} {move_sequence}
        """

        if arguments:
            args = arguments.split(" ", 1)
            if len(args) != 2:
                print("Invalid input format. Usage: cm {sequence_name} {move_sequence}")
            else:
                sequence_name, move_sequence = args
                moves = CubeMoves().add_moves(move_sequence)
                self.data['move_sequences'][sequence_name] = moves
        else:
            print("Invalid input format. Usage: cm {sequence_name} {move_sequence}")

    def _render_cube(self, arguments=None):
        """
        Render Cube
        -rn {cube_name}
        """
        if arguments:
            cube_name = arguments
            if cube_name not in self.data['cubes']:
                print(f"Cube '{cube_name}' does not exist.")
            else:
                self.cube = cube_name
                self.renderer.cube = self.data['cubes'][cube_name].Cube
        else:
            print("Cube name is missing. Usage: rn {cube_name}")

    def _list_cubes(self, arguments=None):
        """
        List Cube(s)
        -ls {o/cube_name}
        """
        if arguments:
            if self.data['cubes'].get(arguments):
                print(self.data['cubes'][arguments].Cube)
            else:
                print(f"Cube '{arguments}' does not exist.")
        else:
            print(self.data['cubes'])

    def _list_move_sequence(self, arguments=None):
        """
        List Move Sequence(s)
        -lm {o/sequence_name}
        """
        if arguments:
            if self.data['move_sequences'].get(arguments):
                print(self.data['move_sequences'][arguments].moves)
            else:
                print(f"Sequence '{arguments}' does not exist.")
        else:
            print(self.data['move_sequences'])

    def _execute_move_sequence(self, arguments=None):
        """
        Execute Move Sequence
        -ex {cube_name} {sequence_name/move_sequence}
        """
        if arguments:
            args = arguments.split(" ", 1)
            if len(args) != 2:
                print("Invalid input format. Usage: ex {cube_name} {sequence_name/move_sequence}")
            else:
                cube_name, move_sequence = args
                if cube_name not in self.data['cubes']:
                    print(f"Cube '{cube_name}' does not exist.")
                elif move_sequence in self.data['move_sequences']:
                    # Execute the predefined move sequence
                    self.data['move_sequences'][move_sequence].execute_moves(self.data['cubes'][cube_name].Cube, copy=True)
                else:
                    # Execute the custom move sequence
                    moves = CubeMoves().add_moves(move_sequence)
                    moves.execute_moves(self.data['cubes'][cube_name].Cube)
        else:
            print("Invalid input format. Usage: ex {cube_name} {sequence_name/move_sequence}")



