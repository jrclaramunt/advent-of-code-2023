import re
from curses.ascii import isdigit

from utils.base import Day


class Day1(Day):

    def __init__(self, args):
        self.calibration_document = list(map(lambda x: x.strip(), args[0]))

    def part1(self):
        total = 0
        for calibration_line in self.calibration_document:
            calibration_digits = list(filter(lambda x: isdigit(x), calibration_line))
            total += int(calibration_digits[0] + calibration_digits[-1])
        return total

    def part2(self):
        total = 0
        for calibration_line in self.calibration_document:
            calibration_digits = list(filter(lambda x: isdigit(x), self.decode_calibration_line(calibration_line)))
            total += int(calibration_digits[0] + calibration_digits[-1])
        return total

    def decode_calibration_line(self, line):
        numbers_with_text = {
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        for key, value in numbers_with_text.items():

        return line