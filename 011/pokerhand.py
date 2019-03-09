import collections


Card = collections.namedtuple("Card", "value, suit")


class PokerHand:
    SUITS = ('S', 'H', 'C', 'D')
    FACE_VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 13}
    HAND_VALUES = {'High Card': 1, 'Pair': 2, 'Two Pair': 3, 'Three of a Kind': 4,
                   'Straight': 5, 'Flush': 6, 'Full House': 7, 'Four of a Kind': 8,
                   'Straight Flush': 9}

    def __init__(self, hand):
        self.cards = []
        if type(hand) == str:
            hand = hand.split()
        for card in hand:
            try:
                value, suit = card[:-1], card[-1]
            except IndexError:
                raise ValueError('Invalid card in hand - {}'.format(card))

            if value not in PokerHand.FACE_VALUES or suit not in PokerHand.SUITS:
                raise ValueError('Invalid card in hand - {}'.format(card))
            self.cards.append(Card(value=value, suit=suit))
        self.cards.sort()

    def call(self, opponent):
        my_hand = sorted(self.cards, reverse=True)
        opponent_hand = sorted(opponent.cards, reverse=True)
        winner = None
        if self._hand_value() == opponent._hand_value():
            card_count = 0
            while not winner:
                my_card = PokerHand.FACE_VALUES[my_hand[card_count].value]
                opponent_card = PokerHand.FACE_VALUES[opponent_hand[card_count].value]
                if my_card > opponent_card:
                    winner = my_hand
                elif my_card < opponent_card:
                    winner = opponent_hand
                else:
                    card_count += 1
            if winner == my_hand:
                return "I win with {} {}".format(self._hand_value(),
                                                 ''.join(my_hand[card_count]))
            elif winner == opponent_hand:
                return "Opponent wins with {} {}".format(opponent._hand_value(),
                                                         ''.join(opponent_hand[card_count]))



    def __str__(self):
        hand_str = []
        for card in self.cards:
            hand_str.append("{}{}".format(card.value, card.suit))
        return " ".join(hand_str)

    def _hand_value(self):
        return "High Card"

if __name__ == '__main__':
    myhand = PokerHand('2C 3H 4S 8C AH')
    opponenthand = PokerHand('2H 3D 5S 9C KD')
    print("My hand is: {}".format(myhand))
    print("Opponent's hand is: {}".format(opponenthand))
