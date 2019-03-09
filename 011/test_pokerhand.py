import pytest

from pokerhand import PokerHand


def test_pokerhand_creates_a_hand_from_string():
    myhand = PokerHand('2H 3D 5S 9C KD')
    assert(type(myhand) == PokerHand)


def test_pokerhand_creates_a_hand_from_list():
    myhand = PokerHand(['2H', '3D', '5S', '9C', 'KD'])
    assert(type(myhand) == PokerHand)


def test_pokerhand_does_not_accept_invalid_hand():
    with pytest.raises(ValueError):
        myhand = PokerHand('13H 3D 5S 9C KD')


def test_string_representation_of_pokerhand():
    myhand = PokerHand(['2H', '3D', '5S', '9C', 'KD'])
    assert(str(myhand) == '2H 3D 5S 9C KD')


def test_highcard_pokerhand_wins():
    high_hand = PokerHand('2C 3H 4S 8C AH')
    low_hand = PokerHand('2H 3D 5S 9C KD')
    assert(high_hand.call(low_hand) == "You Win with High Card AH")


def test_lowhand_loses_to_highcard_pokerhand():
    high_hand = PokerHand('2C 3H 4S 8C AH')
    low_hand = PokerHand('2H 3D 5S 9C KD')
    assert(low_hand.call(high_hand) == "You Lose to High Card AH")
