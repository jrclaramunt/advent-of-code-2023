import functools
import math
import re

from utils.base import Day


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value} = ({self.left}, {self.right})'


class Day8(Day):
    def __init__(self, args):
        self.data = {}
        self.path = list(args[0][0].strip())
        for l in args[0][2:]:
            a = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', l.strip()).groups()
            self.data[a[0]] = Node(a[0], a[1], a[2])
        pass

    def part1(self):
        return self.calculate_steps(initial_node='AAA')

    def part2(self):
        starting_nodes = list(filter(lambda x: x[-1] == 'A', self.data.keys()))
        steps_per_node = []
        for node in starting_nodes:
            steps = self.calculate_steps(initial_node=node, end_node_pattern=r'..Z')
            steps_per_node.append(steps)

        return math.lcm(*steps_per_node)

    def calculate_steps(self, initial_node, end_node_pattern=r'ZZZ'):
        total = 0
        current_node = initial_node
        while not re.match(end_node_pattern, current_node):
            for movement in self.path:
                if movement == 'L':
                    current_node = self.data[current_node].left
                else:
                    current_node = self.data[current_node].right
                total += 1
        return total
