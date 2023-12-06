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
            matching_numbers = list(set(card_data['winning_numbers']) & set(card_data['played_numbers']))
            total += floor(pow(2, len(matching_numbers) - 1))

        return total

    def part2(self):
        for card_id in self.cards.keys():
            self.cards[card_id]['instances'] = 1

        for card_id, card_data in self.cards.items():
            matching_numbers = list(set(card_data['winning_numbers']) & set(card_data['played_numbers']))
            if len(matching_numbers) > 0:
                for i in range(int(card_id) + 1, int(card_id) + len(matching_numbers) + 1):
                    self.cards[str(i)]['instances'] += self.cards[card_id]['instances']

        total = 0
        for a in self.cards.values():
            total += a['instances']

        return total



