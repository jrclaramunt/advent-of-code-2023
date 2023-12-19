from utils.base import Day


class Day9(Day):
    def __init__(self, args):
        self.data = []
        for input_line in args[0]:
            value_history = list(map(lambda x: int(x), input_line.split(' ')))
            steps_sequences = [value_history]
            while True:
                next_sequence = self.get_next_sequence(value_history)
                value_history = next_sequence
                if next_sequence[0] == 0 and next_sequence[-1] == 0:
                    break
                else:
                    steps_sequences.append(next_sequence)

            self.data.append(steps_sequences)

    def part1(self):
        total = 0
        for set_of_sequences in self.data:
            predicted_value = 0
            for sequence in reversed(set_of_sequences):
                predicted_value += sequence[-1]

            total += predicted_value

        return total

    def part2(self):
        total = 0
        for set_of_sequences in self.data:
            predicted_value = 0
            for sequence in reversed(set_of_sequences):
                predicted_value = sequence[0] - predicted_value

            total += predicted_value

        return total

    @staticmethod
    def get_next_sequence(sequence):
        next_sequence = []
        for i in range(len(sequence) - 1):
            next_sequence.append(sequence[i + 1] - sequence[i])
        return next_sequence
