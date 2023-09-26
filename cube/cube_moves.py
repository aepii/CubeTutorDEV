from collections import deque


class CubeMoves:
    def __init__(self):
        self.moves = deque()

    def add_move(self, move):
        self.moves.append(move)

        return self

    def execute_moves(self, cube, solve=True):

        if solve is True:
            while self.moves:
                move = self.moves.popleft()
                self._perform_move(cube, move)

        else:
            if self.moves:
                move = self.moves.popleft()
                self._perform_move(cube, move)

    def _perform_move(self, cube, move):
        faces = ['F', 'B', 'L', 'R', 'U', 'D']

        if "'" not in move and "2" not in move:  # 90 degrees clockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True)
        elif "'" in move:  # 90 degrees counterclockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=False)
        elif "2" in move:  # 180 degrees clockwise
            face = move[0]
            if face in faces:
                self._rotate_cube(cube, face, clockwise=True, double=True)

    @staticmethod
    def _rotate_cube(cube, face, clockwise=True, double=False):

        if clockwise is True and double is False:
            if face == "U":
                front_prev = cube.getFront()
                left_prev = cube.getLeft()
                back_prev = cube.getBack()
                right_prev = cube.getRight()

                upper_prev = cube.getUpper()

                cube.setUpper([
                    [upper_prev[2][0], upper_prev[1][0], upper_prev[0][0]],
                    [upper_prev[2][1], upper_prev[1][1], upper_prev[0][1]],
                    [upper_prev[2][2], upper_prev[1][2], upper_prev[0][2]]
                ])

                cube.setFront([right_prev[0], front_prev[1], front_prev[2]])
                cube.setLeft([front_prev[0], left_prev[1], left_prev[2]])
                cube.setBack([left_prev[0], back_prev[1], back_prev[2]])
                cube.setRight([back_prev[0], right_prev[1], right_prev[2]])

            elif face == "D":
                front_prev = cube.getFront()
                left_prev = cube.getLeft()
                back_prev = cube.getBack()
                right_prev = cube.getRight()

                lower_prev = cube.getLower()

                cube.setLower([
                    [lower_prev[2][0], lower_prev[1][0], lower_prev[0][0]],
                    [lower_prev[2][1], lower_prev[1][1], lower_prev[0][1]],
                    [lower_prev[2][2], lower_prev[1][2], lower_prev[0][2]]
                ])

                cube.setFront([front_prev[0], front_prev[1], left_prev[2]])
                cube.setLeft([left_prev[0], left_prev[1], back_prev[2]])
                cube.setBack([back_prev[0], back_prev[1], right_prev[2]])
                cube.setRight([right_prev[0], right_prev[1], front_prev[2]])

            elif face == "L":
                front_prev = cube.getFront()
                lower_prev = cube.getLower()
                back_prev = cube.getBack()
                upper_prev = cube.getUpper()

                left_prev = cube.getLeft()

                cube.setLeft([
                    [left_prev[2][0], left_prev[1][0], left_prev[0][0]],
                    [left_prev[2][1], left_prev[1][1], left_prev[0][1]],
                    [left_prev[2][2], left_prev[1][2], left_prev[0][2]]
                ])

                cube.setFront([
                    [upper_prev[0][0], front_prev[0][1], front_prev[0][2]],
                    [upper_prev[1][0], front_prev[1][1], front_prev[1][2]],
                    [upper_prev[2][0], front_prev[2][1], front_prev[2][2]]
                ])

                cube.setLower([
                    [front_prev[0][0], lower_prev[0][1], lower_prev[0][2]],
                    [front_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                    [front_prev[2][0], lower_prev[2][1], lower_prev[2][2]]
                ])

                cube.setBack([
                    [back_prev[0][0], back_prev[0][1], lower_prev[2][0]],
                    [back_prev[1][0], back_prev[1][1], lower_prev[1][0]],
                    [back_prev[2][0], back_prev[2][1], lower_prev[0][0]]
                ])

                cube.setUpper([
                    [back_prev[2][2], upper_prev[0][1], upper_prev[0][2]],
                    [back_prev[1][2], upper_prev[1][1], upper_prev[1][2]],
                    [back_prev[0][2], upper_prev[2][1], upper_prev[2][2]]
                ])

            elif face == "R":
                front_prev = cube.getFront()
                lower_prev = cube.getLower()
                back_prev = cube.getBack()
                upper_prev = cube.getUpper()

                right_prev = cube.getRight()

                cube.setRight([
                    [right_prev[2][0], right_prev[1][0], right_prev[0][0]],
                    [right_prev[2][1], right_prev[1][1], right_prev[0][1]],
                    [right_prev[2][2], right_prev[1][2], right_prev[0][2]]
                ])

                cube.setFront([
                    [front_prev[0][0], front_prev[0][1], lower_prev[0][2]],
                    [front_prev[1][0], front_prev[1][1], lower_prev[1][2]],
                    [front_prev[2][0], front_prev[2][1], lower_prev[2][2]]
                ])

                cube.setLower([
                    [lower_prev[0][0], lower_prev[0][1], back_prev[2][0]],
                    [lower_prev[1][0], lower_prev[1][1], back_prev[1][0]],
                    [lower_prev[2][0], lower_prev[2][1], back_prev[0][0]]
                ])

                cube.setBack([
                    [upper_prev[2][2], back_prev[0][1], back_prev[0][2]],
                    [upper_prev[1][2], back_prev[1][1], back_prev[1][2]],
                    [upper_prev[0][2], back_prev[2][1], back_prev[2][2]]
                ])

                cube.setUpper([
                    [upper_prev[0][0], upper_prev[0][1], front_prev[0][2]],
                    [upper_prev[1][0], upper_prev[1][1], front_prev[1][2]],
                    [upper_prev[2][0], upper_prev[2][1], front_prev[2][2]]
                ])

            elif face == "F":
                left_prev = cube.getLeft()
                lower_prev = cube.getLower()
                right_prev = cube.getRight()
                upper_prev = cube.getUpper()

                front_prev = cube.getFront()

                cube.setFront([
                    [front_prev[2][0], front_prev[1][0], front_prev[0][0]],
                    [front_prev[2][1], front_prev[1][1], front_prev[0][1]],
                    [front_prev[2][2], front_prev[1][2], front_prev[0][2]]
                ])

                cube.setLeft([
                    [left_prev[0][0], left_prev[0][1], lower_prev[0][0]],
                    [left_prev[1][0], left_prev[1][1], lower_prev[0][1]],
                    [left_prev[2][0], left_prev[2][1], lower_prev[0][2]]
                ])

                cube.setUpper([
                    [upper_prev[0][0], upper_prev[0][1], upper_prev[0][2]],
                    [upper_prev[1][0], upper_prev[1][1], upper_prev[1][2]],
                    [left_prev[2][2], left_prev[1][2], left_prev[0][2]]
                ])

                cube.setRight([
                    [upper_prev[2][0], right_prev[0][1], right_prev[0][2]],
                    [upper_prev[2][1], right_prev[1][1], right_prev[1][2]],
                    [upper_prev[2][2], right_prev[2][1], right_prev[2][2]]
                ])

                cube.setLower([
                    [right_prev[2][0], right_prev[1][0], right_prev[0][0]],
                    [lower_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                    [lower_prev[2][0], lower_prev[2][1], lower_prev[2][2]]
                ])

            elif face == "B":
                left_prev = cube.getLeft()
                lower_prev = cube.getLower()
                right_prev = cube.getRight()
                upper_prev = cube.getUpper()

                back_prev = cube.getBack()

                cube.setBack([
                    [back_prev[2][0], back_prev[1][0], back_prev[0][0]],
                    [back_prev[2][1], back_prev[1][1], back_prev[0][1]],
                    [back_prev[2][2], back_prev[1][2], back_prev[0][2]]
                ])

                cube.setLeft([
                    [upper_prev[0][2], left_prev[0][1], left_prev[0][2]],
                    [upper_prev[0][1], left_prev[1][1], left_prev[1][2]],
                    [upper_prev[0][0], left_prev[2][1], left_prev[2][2]]
                ])

                cube.setUpper([
                    [right_prev[0][2], right_prev[1][2], right_prev[2][2]],
                    [upper_prev[1][0], upper_prev[1][1], upper_prev[1][2]],
                    [upper_prev[2][0], upper_prev[2][1], upper_prev[2][2]]
                ])

                cube.setRight([
                    [left_prev[0][0], right_prev[0][1], lower_prev[2][2]],
                    [right_prev[1][0], right_prev[1][1], lower_prev[2][1]],
                    [right_prev[2][0], right_prev[2][1], lower_prev[2][0]]
                ])

                cube.setLower([
                    [lower_prev[0][0], lower_prev[0][1], lower_prev[0][2]],
                    [lower_prev[1][0], lower_prev[1][1], lower_prev[1][2]],
                    [left_prev[0][0], left_prev[1][0], left_prev[2][0]]
                ])
