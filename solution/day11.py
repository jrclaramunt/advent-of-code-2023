import bisect

from utils.base import Day


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate):
        return abs(self.x - coordinate.x) + abs(self.y - coordinate.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Day11(Day):
    def __init__(self, args):
        self.grid = []
        self.initial_galaxies = []
        self.rows_with_galaxies = set()
        self.columns_with_galaxies = set()
        self.starting_point = None

        for x in range(len(args[0])):
            l = []
            for y in range(len(args[0][x].strip())):
                value = args[0][x][y]
                l.append(value)
                if value == '#':
                    self.rows_with_galaxies.add(x)
                    self.columns_with_galaxies.add(y)
                    self.initial_galaxies.append(Galaxy(x, y))
            self.grid.append(l)

    def part1(self):
        spaces = 1
        return self.expand(spaces)

    def part2(self):
        spaces = 1000000 - 1
        return self.expand(spaces)

    def expand(self, spaces):
        galaxies = []

        rows = set(range(len(self.grid)))
        rows_to_expand = sorted(rows - self.rows_with_galaxies)

        columns = set(range(len(self.grid[0])))
        columns_to_expand = sorted(columns - self.columns_with_galaxies)

        for galaxy in self.initial_galaxies:
            empy_rows_behind = bisect.bisect_left(rows_to_expand, galaxy.x)
            empy_columns_behind = bisect.bisect_left(columns_to_expand, galaxy.y)

            new_galaxy = Galaxy(galaxy.x + spaces * empy_rows_behind, galaxy.y + spaces * empy_columns_behind)
            galaxies.append(new_galaxy)

        total = 0
        for i in range(len(self.initial_galaxies)):
            for j in range(i + 1, len(galaxies)):
                # print(
                #     f'Galaxies {i + 1} {galaxies[i]} and {j + 1} {galaxies[j]}: {galaxies[i].distance(galaxies[j])}'
                # )
                total += galaxies[i].distance(galaxies[j])
        # too high 906430564650
        # too high 298933222626
        return total
