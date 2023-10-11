from game.model import DirectionModel
from game.model import Location
import random
import os


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def print_map(self):
        for item in range(0, len(self.map)):
            for row in range(0, len(self.map[item])):
                print(self.map[item][row], end=" ")
            print()

    def __zero_to_end(self):
        for item in self.__list_merge:
            if item == 0:
                self.__list_merge.remove(item)
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for item in range(len(self.__list_merge) - 1):
            if self.__list_merge[item] == self.__list_merge[item + 1]:
                self.__list_merge[item] += self.__list_merge[item + 1]
                del self.__list_merge[item + 1]
                self.__list_merge.append(0)

    def __change_row_col(self):
        for row in range(1, len(self.map)):
            for col in range(row, len(self.map)):
                self.map[col][row - 1], self.map[row - 1][col] = self.map[row - 1][col], self.map[col][row - 1]

    def __move_left(self):
        for line in self.map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for line in self.map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self):
        self.__change_row_col()
        self.__move_left()
        self.__change_row_col()

    def __move_down(self):
        self.__change_row_col()
        self.__move_right()
        self.__change_row_col()

    def move(self, dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def __get_empty_loc(self):
        self.__list_empty_location.clear()
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 0:
                    self.__list_empty_location.append(Location(row, col))

    def generate_new_number(self):
        self.__get_empty_loc()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(loc)

    def is_game_over(self):
        if self.__list_empty_location > 0:
            return False

        for r in range(len(self.map)):
            for c in range(r, len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1]:
                    return False

        for c in range(len(self.map)):
            for r in range(len(self.map[c]) - 1):
                if self.map[r][c] == self.map[r + 1][c]:
                    return False
        return True


if __name__ == "__main__":
    g1 = GameCoreController()
    # g1.move_right()
    # g1.move_down()
    g1.move(DirectionModel.UP)
    g1.generate_new_number()
    g1.generate_new_number()
    g1.generate_new_number()
    g1.generate_new_number()
    g1.print_map()
    os.system("whoami")