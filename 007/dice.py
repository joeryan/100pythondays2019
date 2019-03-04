import random

class Die():
  def __init__(self, value):
    self.sides = value

  def roll(self):  
    return random.randint(1, self.sides)
