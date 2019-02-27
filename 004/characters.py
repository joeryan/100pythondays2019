import random

class Character():
  def __init__(self, name, level, attack):
    self.name = name
    self.level = level
    self.health = level * random.randint(1,6)
    self.attack = attack

class Creature(Character):
  def __str__(self):
    return "Creature: {} of level {}".format(self.name, self.level)

class Wizard(Character):
  def __init__(self, name, level, offense, weapon):
    super().__init__(name, level, offense)
    self.weapon = weapon
  def run_away(self):
    print("You run away quickly...")
  def attack_creature(self):
    print("Attacking with {}".format(self.weapon[random.randint(0,len(self.weapon))]))
