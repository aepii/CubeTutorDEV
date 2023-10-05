from .cube import CubeBuilder
from .cube_moves import CubeMoves
from .cube_renderer import CubeRenderer


class Application:
    def __init__(self, MplCanvas):

        self.data = {
            'cubes': {},
            'move_sequences': {}
        }

        self.data['cubes']['Default'] = CubeBuilder(scramble=False)
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
        except:
            command = parse
            arguments = False

        commands = {
            "lr", "c", "rn", "ls"
        }

        if command in commands:
            if command == "lr":
                self._list_current_rendered_cube()
            elif command == "c":

                try:
                    cube_name, move_sequence = arguments.split(" ", 1)
                except:
                    cube_name = arguments
                    move_sequence = False

                self._create_cube(cube_name, move_sequence)

            elif command == "rn":
                self._render_cube(arguments)

            elif command == "ls":
                if arguments:
                    print('yes')
                    self._list_cubes(arguments)
                else:
                    print('no')
                    self._list_cubes()
        else:
            pass

    def _list_current_rendered_cube(self):

        print(self.cube, self.renderer.cube.history)

    def _create_cube(self, cube_name, scramble):

        if scramble is False:
            cube = CubeBuilder(scramble=False)
        else:
            cube = CubeBuilder(scramble)

        self.data['cubes'][cube_name] = cube

    def _render_cube(self, cube_name):
        self.cube = cube_name
        self.renderer.cube = self.data['cubes'][cube_name].Cube

    def _list_cubes(self, cube_name=False):

        if not cube_name:
            print(self.data['cubes'])
        else:
            print(self.data['cubes'][cube_name].Cube.history)

"""
Create Cube
-c {cube_Name} {move_Sequence}

List All Cubes

-ls 

List Specific Cube

-ls {cube_Name}

Create Move Sequence

-cm {sequence_Name} {move_Sequence} 

Execute Move Sequence 

-ex {cube_Name} {sequence_Name/move_Sequence}

Render Cube

-rn {cube_Name}

Remove Cube

-rc {cube_Name}

Remove Move Sequence

-rm {sequence_Name}

List Current Rendered Cube
-lr 


"""
