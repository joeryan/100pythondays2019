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


def test_highhand_calling_lowhand_wins():
    high_hand = PokerHand('2C 3H 4S 8C AH')
    low_hand = PokerHand('2H 3D 5S 9C KD')
    assert(high_hand.call(low_hand) == "Win")


def test_lowhand_calling_highhand_loses():
    high_hand = PokerHand('2C 3H 4S 8C AH')
    low_hand = PokerHand('2H 3D 5S 9C KD')
    assert(low_hand.call(high_hand) == "Lose")

