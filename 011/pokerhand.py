import collections


class Card:
    SUITS = ('S', 'H', 'C', 'D')
    FACE_VALUES = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
                   '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

    def __init__(self, card):
        try:
            value, suit = card[:-1], card[-1]
        except IndexError:
            raise ValueError('Invalid card in hand - {}'.format(card))

        if value not in Card.FACE_VALUES or suit not in Card.SUITS:
            raise ValueError('Invalid card in hand - {}'.format(card))

        self.value = Card.FACE_VALUES[value]
        self.suit = suit
        self.cardstr = card

    def __str__(self):
        return self.cardstr


class PokerHand:

    HAND_VALUES = {'High Card': 1, 'Pair': 2, 'Two Pair': 3, 'Three of a Kind': 4,
                   'Straight': 5, 'Flush': 6, 'Full House': 7, 'Four of a Kind': 8,
                   'Straight Flush': 9}

    def __init__(self, hand):
        self.cards = []
        if type(hand) == str:
            hand = hand.split()
        for card in hand:

            self.cards.append(Card(card))
        self.cards.sort(key=lambda x: x.value)

    def call(self, opponent):
        if self.get_hand_value() > opponent.get_hand_value():
            return "Win"
        if self.get_hand_value() < opponent.get_hand_value():
            return "Lose"

        my_hand = sorted(self.cards, key=lambda x: x.value, reverse=True)
        opponent_hand = sorted(opponent.cards, key=lambda x: x.value, reverse=True)
        winner = None
        my_value = self.get_hand_value()
        opponent_value = opponent.get_hand_value()
        if my_value == opponent_value:
            card_count = 0
            while not winner:
                if my_hand[card_count].value > opponent_hand[card_count].value:
                    winner = my_hand
                elif my_hand[card_count].value < opponent_hand[card_count].value:
                    winner = opponent_hand
                else:
                    card_count += 1
            winning_hand = []
            for i in range(0,card_count):
                winning_hand.append(str(winner[i]))
            if winner == my_hand:
                return "Win"
                # with {} {}".format(my_value[0],''.join(str(winning_hand[-(my_value[1]):])))
            elif winner == opponent_hand:
                return "Lose"
                       # "Opponent wins with {} {}".format(opponent_value[0],''.join(winning_hand[-(my_value[1]):]))

    def __str__(self):
        hand_str = []
        for card in self.cards:
            hand_str.append(str(card))
        return " ".join(hand_str)

    def get_hand_value(self):
        flush, straight = False, False

        return "High Card", 1

    def score_hand(self):
        score = {}
        score['cards'] = None
        score['value'] = collections.defaultdict(lambda: 0)
        for i, card in enumerate(self.cards):
            if card.value in self.cards[i+1:]:
                score.value[card.value] += 1
        return score


if __name__ == '__main__':
    myhand = PokerHand('2C 8H 4S 8C AH')
    myscore = ''.join([x for x in myhand.score_hand()['value']])
    opponenthand = PokerHand('2H 3D 5S 9C KD')
    print("My hand is: {}".format(myhand))
    print("My score is : {}".format(myscore))
    print("Opponent's hand is: {}".format(opponenthand))
