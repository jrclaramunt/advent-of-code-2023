import re

from utils.base import Day


class Day6(Day):
    def __init__(self, args):
        self.time_data = re.match(r'Time: +(.*)', args[0][0].strip()).groups()[0]
        self.record_distance_data = re.match(r'Distance: +(.*)', args[0][1].strip()).groups()[0]

    def part1(self):
        times = list(map(lambda x: int(x), re.split(r' +', self.time_data.strip())))
        record_distances = list(map(lambda x: int(x), re.split(r' +', self.record_distance_data.strip())))

        total = 1
        for i in range(len(times)):
            time = times[i]
            record_distance = record_distances[i]

            record_breaks = 0
            for speed in range(time):
                distance = speed * (time - speed)
                if distance > record_distance:
                    record_breaks += 1

            total *= record_breaks

        return total

    def part2(self):
        time = int(self.time_data.strip().replace(' ', ''))
        record_distance = int(self.record_distance_data.strip().replace(' ', ''))

        record_breaks = 0
        for speed in range(time):
            distance = speed * (time - speed)
            if distance > record_distance:
                record_breaks += 1

        return record_breaks

