import re
import sys

from utils.base import Day


class Day5(Day):
    def __init__(self, args):
        seeds_data = re.match(r'seeds: +(.+)', args[0][0].strip()).groups()[0]
        self.seeds = list(map(lambda x: int(x), re.split(r' +', seeds_data)))

        self.map_data = args[0][2:]
        pass

    def part1(self):
        indexes = [i for i in range(len(self.map_data)) if self.map_data[i] == '\n']
        data = []
        current_index = 0
        for i in indexes:
            data.append(self.map_data[current_index:i])
            current_index = i + 1
        data.append(self.map_data[current_index:])

        result = sys.maxsize
        for seed in self.seeds:
            print(f'Seed: {seed}')
            seed_destination = seed
            for map_data in data:
                name = map_data[0].strip()
                for map_range in map_data[1:]:
                    range_data = list(map(lambda x: int(x), re.split(r' +', map_range)))
                    destination = (range_data[0], range_data[0] + range_data[2])
                    origin = (range_data[1], range_data[1] + range_data[2])

                    if origin[0] <= seed_destination <= origin[1]:
                        seed_destination = destination[0] + seed_destination - origin[0]
                        break

                print(f'seed value for {name}: {seed_destination}')
            if seed_destination <= result:
                result = seed_destination

        return result

    def part2(self):
        indexes = [i for i in range(len(self.map_data)) if self.map_data[i] == '\n']
        data = []
        current_index = 0
        for i in indexes:
            data.append(self.map_data[current_index:i])
            current_index = i + 1
        data.append(self.map_data[current_index:])

        result = sys.maxsize
        cache = {}
        iter = 1
        for i in range(0, len(self.seeds), 2):
            for j in range(self.seeds[i+1]):
                # print(f'Seed: {self.seeds[i] + j}')

                seed_destination = self.seeds[i] + j
                print(f'Iter: {iter}')

                if cache.get(seed_destination) is not None:
                    seed_destination = cache[seed_destination]
                else:
                    for map_data in data:
                        name = map_data[0].strip()
                        for map_range in map_data[1:]:
                            range_data = list(map(lambda x: int(x), re.split(r' +', map_range)))
                            destination = (range_data[0], range_data[0] + range_data[2])
                            origin = (range_data[1], range_data[1] + range_data[2])

                            if origin[0] <= seed_destination <= origin[1]:
                                seed_destination = destination[0] + seed_destination - origin[0]
                                cache[self.seeds[i] + j] = seed_destination
                                break

                        # print(f'seed value for {name}: {seed_destination}')

                if seed_destination <= result:
                    result = seed_destination
                iter += 1

        return result

