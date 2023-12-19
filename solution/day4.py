import re
from math import floor

from utils.base import Day


class Day4(Day):
    def __init__(self, args):
        self.cards = {}
        regex = r'Card +(\d+): +(.*)\| +(.*)'

        for card in args[0]:
            card_data = re.match(regex, card.strip()).groups()
            card_id = card_data[0]

            self.cards[card_id] = {}
            self.cards[card_id]['winning_numbers'] = list(map(lambda x: int(x), re.split(r' +', card_data[1].strip())))
            self.cards[card_id]['played_numbers'] = list(map(lambda x: int(x), re.split(r' +', card_data[2].strip())))

    def part1(self):
        total = 0
        for card_data in self.cards.values():
            n_of_matching_numbers = self.matching_numbers(card_data)
            total += floor(pow(2, n_of_matching_numbers - 1))

        return total

    def part2(self):
        n_of_instances = {}
        for card_id in self.cards.keys():
            n_of_instances[card_id] = 1

        for card_id, card_data in self.cards.items():
            n_of_matching_numbers = self.matching_numbers(card_data)
            if n_of_matching_numbers > 0:
                for i in range(int(card_id) + 1, int(card_id) + n_of_matching_numbers + 1):
                    n_of_instances[str(i)] += n_of_instances[card_id]

        return sum(n_of_instances.values())

    @staticmethod
    def matching_numbers(card_data):
        return len(list(set(card_data['winning_numbers']) & set(card_data['played_numbers'])))
