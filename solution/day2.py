import re
from functools import reduce

from utils.base import Day


class CubeData:
    def __init__(self, amount, color):
        self.amount = int(amount)
        self.color = color

    def is_valid(self, amount):
        return self.amount <= amount

    def __repr__(self):
        return f'{self.amount} {self.color}'


class Day2(Day):
    def __init__(self, args):
        self.games_record = {}
        for record in args[0]:
            game_record_data = re.match(r'Game (\d+): (.*)', record.strip()).groups()
            game_id = game_record_data[0]
            self.games_record[game_id] = list(set())
            game_record_sets = game_record_data[1].split(';')

            for game_record_set in game_record_sets:
                cubes_set = re.findall(r'(\d+) ([a-z]+),?', game_record_set.strip())
                cube_set = set()
                for data in cubes_set:
                    cube_data = CubeData(data[0], data[1])
                    cube_set.add(cube_data)
                self.games_record[game_id].append(cube_set)

    def part1(self):
        available_cube_set = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        total = 0
        for game_id, cubes_set in self.games_record.items():
            valid_play = True
            for cube_set in cubes_set:
                for cube in cube_set:
                    if not cube.is_valid(available_cube_set[cube.color]):
                        valid_play = False
            if valid_play:
                total += int(game_id)

        return total

    def part2(self):
        total = 0
        for cubes_sets in self.games_record.values():
            total_cubes_per_game = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for cube_set in cubes_sets:
                for cube in cube_set:
                    if total_cubes_per_game[cube.color] <= cube.amount:
                        total_cubes_per_game[cube.color] = cube.amount

            total += reduce(lambda x, y: x * y, total_cubes_per_game.values())

        return total
