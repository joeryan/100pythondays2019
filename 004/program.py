import characters
import random

def print_header():
  print("---------------------")
  print("     Wizard game")
  print("---------------------\n")

def game_loop():
  creatures = [
    characters.Creature('bat', 1, 2), 
    characters.Creature('tiger', 4, 6), 
    characters.Creature('beholder', 12, 8), 
    characters.Creature('dragon', 50, 12), 
    characters.Creature('Evil wizard', 1000, 4),
  ]
  hero = characters.Wizard('Magilus', 20, 4, ["dagger","Fireball", "Magic Missle"])

  exit_game = False
  while not exit_game:
    if random.randint(1,50) >= 5:
      active_creature = random.choice(creatures)
      print("You see a {} glaring at you".format(active_creature))
    else:
      print("Nothing much is around you right now")
    choice = input("Do you want to [a]ttack, [l]ook around, [r]un away, or [q]uit the game? ").lower()
    if choice == 'q':
      exit_game = True
    elif choice == 'a':
      hero.attack_creature()
    elif choice == 'l':
      print("taking a look around...")
      for creature in creatures:
        print("In the distance you see:")
        print(creature)
    elif choice == 'r':
      hero.run_away()
    else:
      print("You really only have those four choices.")
  print("Thanks for playing!")

def main():
  print_header()
  game_loop()

if __name__ == '__main__':
  main()
