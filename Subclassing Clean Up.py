#!/usr/bin/env python3

class NPC:
  def __init__(self, name, attack_dice, defence_dice, body, mind):
   
    # Name
    self.name = name

    # Attack and Defence
    self.current_attack = attack_dice
    self.max_attack = attack_dice
    self.current_defence = defence_dice
    self.max_defence = defence_dice

    # Body Points and status
    self.max_body = body
    self.current_body = body
    self.status_body = "Alive"

    # Mind Points and status
    self.max_mind = mind
    self.current_mind = mind
    self.status_mind = "Normal"

  # Damage to Body Points
  def take_damage_body(self, body_damage_value):
    self.body_damage_value = body_damage_value
    self.current_body -= self.body_damage_value
    print(f"\n{self.name} takes {self.body_damage_value} to their Body!")

    # When Body Points reach 0
    if self.current_body <= 0:
      self.current_body = 0
      self.body_status = "Dead"
      return self.body_status

  # Player taking damage to mind points
  def take_damage_mind(self, mind_damage_value):
    self.mind_damage_value = mind_damage_value
    self.current_mind -= self.mind_damage_value
    print(f"\n{self.name} takes {self.mind_damage_value} to their Mind!")

    # When Player Mind Points reach 0
    if self.current_body <= 0:
      self.current_body = 0
      self.body_status = "In Shock"
      return self.body_status
     
  # Healing Body Points
  def heal_body(self, body_heal_value):
    self.body_heal_value = body_heal_value
    self.current_body += self.body_heal_value

    # Over healing Prevention
    if self.current_body > self.max_body:
      self.current_body = self.max_body
      print(f"{self.name} has had their Body restored to {self.max_body}")
    else:
      print(f"{self.name} has had their Body restored to {self.current_body}")

  # Healing Mind Points
  def heal_mind(self, mind_heal_value):
    self.mind_heal_value = mind_heal_value
    self.current_mind += self.mind_heal_value

    # Over healing Prevention
    if self.current_mind > self.max_mind:
      self.current_mind = self.max_mind
      print(f"{self.name} has had their Mind restored to {self.max_mind}")
    else:
      print(f"{self.name} has had their Mind restored to {self.current_mind}")


class PLAYER:
  def __init__(self, name, movement_dice, attack_dice, defence_dice, body, mind):
    super().__init__(name,attack_dice, defence_dice, body, mind)
    self.movement_dice = movement_dice

class MONSTER:
  def __init__(self, name, movement, attack_dice, defence_dice, body, mind):
    super().__init__(name, attack_dice, defence_dice, body, mind)
    self.movement = movement
    
# Setting the Players stats
# Player Name
def get_player_name():
  name = input(f"\nEnter Name of player in party (Q to stop adding more): ").lower()
  print("")
  return name

# Player Movement Dice count
def get_player_movement_dice():
  while True:
    try:
      movement_dice = int(input("Enter Player's Movement Dice count: "))
    except ValueError:
      print("Invalid Movement Dice count. Please enter a number")
    else:
      break
  return movement_dice

# Player Attack Dice count
def get_player_attack_dice():
  while True:
    try:
      attack_dice = int(input("Enter Player's Attack Dice count: "))
    except ValueError:
      print("Invalid Attack Dice count. Please enter a number")
    else:
      break
  return attack_dice

# Player defence Dice count
def get_player_defence_dice():
  while True:
    try:
      defence_dice = int(input("Enter Player's Defence Dice count: "))
    except ValueError:
      print("Invalid Defence Dice count. Please enter a number")
    else:
      break
  return defence_dice

# Player Body Points
def get_player_body():
  while True:
    try:
      body = int(input("Enter Player's Body Point total: "))
    except ValueError:
      print("Invalid Body Point total. Please enter a number")
    else:
      break
  return body

# Player Mind Points
def get_player_mind():
  while True:
    try:
      mind = int(input("Enter Player's Mind Point total: "))
    except ValueError:
      print("Invalid Mind Point total. Please enter a number")
    else:
      break
  return mind

# Creating the player
def create_player(name, movement_dice, attack_dice, defence_dice, body, mind):
  player = PLAYER(name, movement_dice, attack_dice, defence_dice, body, mind)
  return player

# Print list of current party memebers and their status
def print_party_status(party):
  print("\nCurrent Party Status:")
  for k, v in party.items():
    if party[k].body_status == "Alive":
      print(f"\nName: {party[k].name} \nMovement: {party[k].current_movement}, Attack: {party[k].current_attack}, Defence: {party[k].current_defence} \nBody: {party[k].current_body}/{party[k].max_body} - {party[k].body_status},  Mind: {party[k].current_mind}/{party[k].max_mind} - {party[k].mind_status}")
    else:
      print(f"\nName: {party[k].name} - {party[k].body_status}")

# Setting the Monsters stats
# Monster Name
def get_monster_name():
  name = input(f"\nEnter Name of monster in encounter (Q to stop adding more): ").lower()
  print("")
  return name

# Monster Movement count
def get_monster_movement():
  while True:
    try:
      movement = int(input("Enter Monster's Movement count: "))
    except ValueError:
      print("Invalid Movement count. Please enter a number")
    else:
      break
  return movement

# Monster Attack Dice count
def get_monster_attack_dice():
  while True:
    try:
      attack_dice = int(input("Enter Monster's Attack Dice count: "))
    except ValueError:
      print("Invalid Attack Dice count. Please enter a number")
    else:
      break
  return attack_dice

# Monster defence Dice count
def get_monster_defence_dice():
  while True:
    try:
      defence_dice = int(input("Enter Monster's Defence Dice count: "))
    except ValueError:
      print("Invalid Defence Dice count. Please enter a number")
    else:
      break
  return defence_dice

# Monster Body Points
def get_monster_body():
  while True:
    try:
      body = int(input("Enter Monster's Body Point total: "))
    except ValueError:
      print("Invalid Body Point total. Please enter a number")
    else:
      break
  return body

# Monster Mind Points
def get_monster_mind():
  while True:
    try:
      mind = int(input("Enter Monster's Mind Point total: "))
    except ValueError:
      print("Invalid Mind Point total. Please enter a number")
    else:
      break
  return mind

# Creating the monster
def create_monster(name, movement, attack_dice, defence_dice, body, mind):
  monster = MONSTER(name, movement, attack_dice, defence_dice, body, mind)
  return monster

# Print list of current encounter members and their status
def print_encounter_status(encounter):
  print("\nCurrent Encounter Status:")
  for k, v in encounter.items():
    if encounter[k].body_status == "Alive":
      print(f"\nName: {encounter[k].name} \nMovement: {encounter[k].current_movement}, Attack: {encounter[k].current_attack}, Defence: {encounter[k].current_defence} \nBody: {encounter[k].current_body}/{encounter[k].max_body} - {encounter[k].body_status},  Mind: {encounter[k].current_mind}/{encounter[k].max_mind} - {encounter[k].mind_status}")
    else:
      print(f"\nName: {encounter[k].name} - {encounter[k].body_status}")

# Get Target player
def get_target_player(party):
    while True:
        player = input("Enter the name of the player to target: ").lower()
        if player in party:
            return party[player]
        else:
            print("Invalid player name. Please try again.")

# Get target monster
def get_target_monster(encounter):
  while True:
    monster = input("Enter the name of the monster to target: ").lower()
    if monster in encounter:
      return encounter[monster]
    else:
      print("Invalid monster name. Please try again.")

# handling player menu
def handling_player_menu():
    print("\nPlayer Management Menu:")
    print("1. Damage Body")
    print("2. Damage Mind")
    print("3. Heal Body")
    print("4. Heal Mind")
    print("5. Back to Main Menu")
    option = input("Choose an option: ")
    return option

# handling monster menu
def handling_monster_menu():
    print("\nMonster Management Menu:")
    print("1. Damage Body")
    print("2. Damage Mind")
    print("3. Heal Body")
    print("4. Heal Mind")
    print("5. Back to Main Menu")
    option = input("Choose an option: ")
    return option

# Main function to manage players and monsters
def player_management(party):
    # Setup phase
    while True:
        player_name = get_player_name()
        if player_name == "q":
            break
        else:
            player_attack = get_player_attack_dice()
            player_defence = get_player_defence_dice()
            player_movement = get_player_movement_dice()
            player_body = get_player_body()
            player_mind = get_player_mind()
            player = create_player(player_name, player_movement, player_attack, player_defence, player_body, player_mind)
            party.update({player.name: player})
            print_party_status(party)
    # Action phase
    while True:
        print_party_status(party)
        print_encounter_status(encounter)
        option = handling_player_menu()
        if option == "1":
            target = get_target_player(party)
            dmg = int(input("Enter body damage: "))
            target.take_damage_body(dmg)
        elif option == "2":
            target = get_target_player(party)
            dmg = int(input("Enter mind damage: "))
            target.take_damage_mind(dmg)
        elif option == "3":
            target = get_target_player(party)
            heal = int(input("Enter body healing: "))
            target.heal_body(heal)
        elif option == "4":
            target = get_target_player(party)
            heal = int(input("Enter mind healing: "))
            target.heal_mind(heal)
        elif option == "5":
            break
        else:
            print("Invalid option.")

def monster_management(encounter):
    # Setup phase
    while True:
        monster_name = get_monster_name()
        if monster_name == "q":
            break
        else:
            monster_attack = get_monster_attack_dice()
            monster_defence = get_monster_defence_dice()
            monster_movement = get_monster_movement()
            monster_body = get_monster_body()
            monster_mind = get_monster_mind()
            monster = create_monster(monster_name, monster_movement, monster_attack, monster_defence, monster_body, monster_mind)
            encounter.update({monster.name: monster})
            print_encounter_status(encounter)
    # Action phase
    while True:
        print_party_status(party)
        print_encounter_status(encounter)
        option = handling_monster_menu()
        if option == "1":
            target = get_target_monster(encounter)
            dmg = int(input("Enter body damage: "))
            target.take_damage_body(dmg)
        elif option == "2":
            target = get_target_monster(encounter)
            dmg = int(input("Enter mind damage: "))
            target.take_damage_mind(dmg)
        elif option == "3":
            target = get_target_monster(encounter)
            heal = int(input("Enter body healing: "))
            target.heal_body(heal)
        elif option == "4":
            target = get_target_monster(encounter)
            heal = int(input("Enter mind healing: "))
            target.heal_mind(heal)
        elif option == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    print("\n")
    print("Welcome to the Hero Quest monster and player tracker!")
    print("\n")

    party = {}
    encounter = {}
    
    while True:
        choice = input("\nMain Menu:\n1. Player Management\n2. Monster Management\n3. Exit\nChoose an option: ")
        if choice == "1":
            player_management(party)
        elif choice == "2":
            monster_management(encounter)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")
    