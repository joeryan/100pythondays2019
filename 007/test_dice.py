import pytest
import dice

@pytest.fixture
def die_6():
  return dice.Die(6)

def test_dice_can_roll_random(die_6):
  result = die_6.roll()
  assert result >= 1
  assert result <= 6 

def test_2_die_rolls_not_equal(die_6):
  result1 = die_6.roll()
  result2 = die_6.roll()
  if result2 == result1:
    result2 = die_6.roll()
  assert result1 != result2
